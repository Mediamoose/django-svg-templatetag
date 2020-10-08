=====
Usage
=====

To use Django SVG templatetag in a project::

    {% load svg %}

Then use it in a project::

    {% load svg %}
    
    {% svg path [as varname] %}
   
Examples::

    {% svg "myapp/icons/icon.svg" %}
    {% svg variable_with_path %}
    {% svg "myapp/icons/icon.svg" as icon_svg_content %}
    {% svg variable_with_path as varname %}
