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

This `Ansible role`_ will install Python 3 and the ``pip`` and ``virtualenv``
utilities. The new version of Python is installed independently of the existing
system Python installation.

Although the ``pip`` and ``virtualenv`` command-line tools will be installed,
the recommended way to invoke them is as modules to ensure that the expected
version is used:

.. code-block:: console

    $ python3.6 -m pip install <package>
    $ python3.6 -m venv <dir>

By default, Python is installed from packages. If the ``python3_pyenv`` 
variable is set, `pyenv`_ will be installed and then used to install the 
requested Python version, from source if necessary. The role will *not* 
activate the new Python; see the `pyenv`_ documentation for ways to do this.

The role currently assumes that the user's login shell is ``bash`` and modifies
startup files accordingly. 

This role is also available on `Ansible Galaxy`_.


==============
Role Variables
==============

- ``python3_command``: Python command name
- ``python3_bashrc``: login file to modify; defaults to ``bash_profile``
- ``python3_local``: local binary directory; system-dependent
- ``python3_pyenv``: Python version to install using `pyenv`_


================
Example Playbook
================

.. code-block:: yaml

    - hosts: all
      
      roles:
        - name: python3
          python3_pyenv: "3.6.4"
