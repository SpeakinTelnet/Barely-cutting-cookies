#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import {{ cookiecutter.main_module_name }}

# -- Project configuration ---------------------------------------------

project = '{{ cookiecutter.project_name }}'
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.user }}"
author = "{{ cookiecutter.user }}"

# The short X.Y version.
version = {{ cookiecutter.project_name }}.__version__
# The full version, including alpha/beta/rc tags.
release = {{ cookiecutter.project_name }}.__version__


# -- Language configuration ---------------------------------------------

language = 'en'
spelling_lang='en_US'
spelling_word_list_filename='wordlist.txt'
spelling_show_suggestions=True


# -- Extensions configuration ---------------------------------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.doctest',
              'sphinxcontrib.spelling']


# -- File structure configuration ---------------------------------------------

source_suffix = '.rst'

# The master toctree document.
root_doc = 'index'

# Directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Format configuration ---------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
