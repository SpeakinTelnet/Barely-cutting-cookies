#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.scope }}' == 'personnal':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')
        remove_file('CONTRIBUTING.rst')
        remove_file('docs/contributing.rst')
        remove_file('HISTORY.rst')
        remove_file('docs/history.rst')        
