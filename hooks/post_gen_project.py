import os
import shutil

REMOVE_PATHS = [
    {% if cookiecutter.private_repo == "y" %}
    'CONTRIBUTING.rst',
    'HISTORY.rst',
    'AUTHORS.rst',
    {% endif %}
    {% if (cookiecutter.use_documentation == "n" or cookiecutter.private_repo == "y") %}
    'docs',
    'readthedocs.yml',
    {% endif %}
    {% if cookiecutter.use_brownie == "n" %}
    'contracts',
    'build',
    'interfaces',
    'reports',
    'scripts',
    {% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
