import re

from django import template
from django.contrib.staticfiles import finders
from django.forms.utils import flatatt
from django.template.base import token_kwargs
from django.utils.safestring import mark_safe


register = template.Library()


def get_svg(path, **kwargs):
    if not re.search(r'\.svg$', path):
        raise ValueError('SVG template nodes must be given a path to a SVG file to return.')  # NOQA

    fullpath = finders.find(path)

    if fullpath is None:
        raise IOError('SVG file ({}) not found.'.format(fullpath))

    with open(fullpath, 'r') as fd:
        content = fd.read()

    return mark_safe(re.sub(r'(<svg[^>]*)', r'\1{}'.format(flatatt(kwargs)),
                            content, flags=re.MULTILINE))


class SvgNode(template.Node):
    def __init__(self, varname=None, path=None, **kwargs):
        if path is None:
            raise template.TemplateSyntaxError(
                'SVG template nodes must be given a path to a SVG file to return.')  # NOQA
        self.path = path
        self.varname = varname
        self.kwargs = kwargs

    def render(self, context):
        path = self.path.resolve(context)

        content = get_svg(path, **{
            x: y.resolve(context) for x, y in self.kwargs.items()
        })

        if self.varname is None:
            return content
        context[self.varname] = mark_safe(content)
        return ''

    @classmethod
    def handle_token(cls, parser, token):
        """
        Class method to parse prefix node and return a Node.
        """
        bits = token.split_contents()

        if len(bits) < 2:
            raise template.TemplateSyntaxError(
                '"%s" takes at least one argument (path to file)' % bits[0])

        path = parser.compile_filter(bits[1])

        if len(bits) >= 2 and bits[-2] == 'as':
            varname = bits[-1]
            bits = bits[:-2]
        else:
            varname = None

        return cls(varname, path, **token_kwargs(bits[2:], parser))


@register.tag('svg')
def do_svg(parser, token):
    """
    Inject static svg file contents

    Usage::

        {% svg path [as varname] %}

    Examples::

        {% svg "myapp/icons/icon.svg" %}
        {% svg variable_with_path %}
        {% svg "myapp/icons/icon.svg" as icon_svg_content %}
        {% svg variable_with_path as varname %}
    """
    return SvgNode.handle_token(parser, token)
