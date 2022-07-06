.. highlight:: shell

============
Contributing
============

Contributions are welcome, either in the form of reports or fixes. Refer to the 
`GitHub repo <https://github.com/{{ cookiecutter.user }}/{{ cookiecutter.project_name }}>`_ for issues and
pull requests.


Report Bugs
-----------

If you are reporting a bug, please include:

* Your operating system.
* Detailed steps to reproduce the bug.


Enhancement Guidelines
----------------------

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Pull Request Guidelines
-----------------------

Your pull request should pass the *nox* test. 

nox will run ``black``, ``flake8``, ``pytest``, and regenerate the docs

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

CircleCI will then deploy to PyPI if tests pass.
