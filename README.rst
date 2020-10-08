======================
Django SVG templatetag
======================

.. image:: https://badge.fury.io/py/django-svg-templatetag.png
    :target: https://badge.fury.io/py/django-svg-templatetag

.. image:: https://travis-ci.org/Mediamoose/django-svg-templatetag.png?branch=master
    :target: https://travis-ci.org/Mediamoose/django-svg-templatetag

.. image:: https://img.shields.io/codecov/c/github/Mediamoose/django-svg-templatetag.svg
    :target: https://codecov.io/gh/Mediamoose/django-svg-templatetag

.. image:: https://readthedocs.org/projects/django-svg-templatetag/badge/?version=latest
    :target: https://django-svg-templatetag.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Inject a SVG file into your Django template.

Documentation
-------------

The full documentation is at https://django-svg-templatetag.readthedocs.org.

Quickstart
----------

Install Django SVG templatetag::

    pip install django-svg-templatetag

Then use it in a project::

    {% load svg %}
    
    {% svg path [as varname] %}
   
Examples:

    {% svg "myapp/icons/icon.svg" %}
    {% svg variable_with_path %}
    {% svg "myapp/icons/icon.svg" as icon_svg_content %}
    {% svg variable_with_path as varname %}

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
