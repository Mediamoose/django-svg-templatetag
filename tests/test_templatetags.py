#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-svg-templatetag
---------------------------

Tests for `django-svg-templatetag`.
"""

from django.template import Context, Template
from django.template.exceptions import TemplateSyntaxError
from django.test.testcases import TestCase

from svg_templatetag.templatetags.svg import SvgNode


class SvgTagsTestCase(TestCase):
    context = Context()
    svg_file = 'user.svg'

    def test_svg_path(self):
        with self.assertRaises(TemplateSyntaxError):
            Template('{% load svg %}{% svg  %}')

        with self.assertRaises(ValueError):
            t = Template('{% load svg %}{% svg "test.jpg" %}')
            t.render(self.context)

        with self.assertRaises(IOError):
            t = Template('{% load svg %}{% svg "test.svg" %}')
            t.render(self.context)

        with self.assertRaises(TemplateSyntaxError):
            node = SvgNode()
            node.__init__(node, path=None)

    def test_do_svg(self):
        t = Template('{{% load svg %}}{{% svg "{}" as test_svg %}}'.format(
            self.svg_file))
        t.render(self.context)
        assert 'test_svg' in self.context

        t = Template('{{% load svg %}}{{% svg "{}" %}}'.format(self.svg_file))
        result = t.render(self.context)
        assert '<svg' in result
