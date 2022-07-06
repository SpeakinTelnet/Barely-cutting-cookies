#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

{% if cookiecutter.scope == 'public' -%}
with open('HISTORY.rst') as history_file:
    history = history_file.read()
{% endif -%}


requirements = []

test_requirements = ['pytest>=3',]

setup(
    author="{{ cookiecutter.user }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=requirements,
    license='License :: OSI Approved :: MIT License',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_name }}',
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(include=['{{ cookiecutter.main_module_name }}.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.user }}/{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
