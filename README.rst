#######
python3
#######
.. |travis.png| image:: https://travis-ci.org/mdklatt/ansible-python3-role.png?branch=master
   :alt: Travis CI build status
   :target: `travis`_
.. _travis: https://travis-ci.org/mdklatt/ansible-python3-role
.. _Ansible role: http://docs.ansible.com/ansible/playbooks_roles.html#roles
.. _Ansible Galaxy: https://galaxy.ansible.com/mdklatt/python3

.. _Ansible: http://docs.ansible.com/ansible
.. _pyenv: https://github.com/pyenv/pyenv


This `Ansible`_ role will install Python 3, making sure that ``pip`` is
installed. The new version of Python is installed independently of the existing
system Python installation.

After installation, the recommended way to invoke pip is as a module. This
ensures that the expected version is used.

.. code-block:: console

    $ python3.6 -m pip install <package>


By default, Python is installed from packages. If the ``python3_pyenv`` 
variable is set, `pyenv`_ will be installed and then used to install the 
requested Python version, from source if necessary. The role will *not* 
activate the new Python; see the `pyenv`_ documentation for ways to do this.


==============
Role Variables
==============

- ``python3_command``: Python command name
- ``python3_local``: local binary directory; system-dependent
- ``python3_pyenv``: Python version to install using `pyenv`_


================
Example Playbook
================

.. code-block:: yaml

    - hosts: all
      
      roles:
        - name: python3
          python3_pyenv: "3.6.2"
