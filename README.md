# Test Coverage with Django

## What is this?

This is a simple package that adds support for coverage reporting to Django's test command.

## Quickstart

- add `django_coverage` to your project's INSTALLED_APPS
- run `./manage.py test --coverage` to output coverage report
- For xml output add `--xml` argument
- For html output add `--html` argument
- For custom settings create a `.coveragerc`