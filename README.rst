#######
python3
#######

.. |travis.png| image:: https://travis-ci.org/mdklatt/ansible-python3-role.png?..     
   :alt: Travis CI build status
   :target: `travis`_
.. _travis: https://travis-ci.org/mdklatt/ansible-python3-role
.. _Ansible role: http://docs.ansible.com/ansible/playbooks_roles.html#roles
.. _Ansible Galaxy: https://galaxy.ansible.com/mdklatt/python3
.. _pyenv: https://github.com/pyenv/pyenv

|travis.png|

This `Ansible role`_ will install Python 3, ``pip``, and``virtualenv``. The
new Python is installed independently of the existing system Python
installation.

Although the ``pip`` and ``virtualenv`` command-line tools will be installed,
the recommended way to invoke them is as modules to ensure that the expected
version is used:

.. code-block:: console

    $ python3.6 -m pip install <package>
    $ python3.6 -m venv <dir>

The role currently assumes that the user's login shell is ``bash`` and modifies
startup files accordingly.

By default, Python is installed from packages. If the ``python3_pyenv``
variable is set, `pyenv`_ will be installed and then used to install the
requested Python version, from source if necessary. A `pyenv`_ install is only
visible for the current Ansible user (the login user by default). The role will
*not* activate the new Python; see the `pyenv`_ documentation for ways to do
this.

This role is also available on `Ansible Galaxy`_.


==============
Using the Role
==============

Role Variables
==============

- ``python3_command``: Python command name
- ``python3_bashrc``: login file to modify; defaults to ``bash_profile``
- ``python3_local``: local binary directory; system-dependent
- ``python3_pyenv``: Python version to install using `pyenv`_


Example Playbook
================

.. code-block:: yaml

    - hosts: all
      
      roles:
        - name: python3
          python3_pyenv: "3.6.4"


===========
Development
===========
.. _Molecule: https://molecule.readthedocs.io/en/stable/getting-started.html#run-a-full-test-sequence

Use the ``task`` script to run development tasks:

- ``dev``: Create the local development environment
- ``test``: Run the `Molecule`_ test suite
