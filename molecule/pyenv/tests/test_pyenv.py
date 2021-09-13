""" Test suite for the Molecule 'pyenv' scenario.

"""
from os import environ
from testinfra.utils.ansible_runner import AnsibleRunner

import pytest


# Create the `host` fixture parametrized over all configured test platforms.
# Each `host` is a Testinfra Host instance. The inventory is created by the
# Molecule framework, so this test suite must be run via *e.g.* `molecule test`
# and not `pytest`.
runner = AnsibleRunner(environ["MOLECULE_INVENTORY_FILE"])
testinfra_hosts = runner.get_hosts("all")


def pyenv(command: str) -> str:
    """ Wrap a command to use the pyenv environment.

    :param command: original command
    :return: modified command
    """
    # Testinfra uses a separate /bin/sh invocation for every remote command,
    # and ~/.profile is not being sourced, so it needs to be prepended to every
    # command.
    return f". ~/.profile && {command}"


@pytest.fixture(scope="module")
def python(host):
    """ Enable the pyenv Python.

    """
    version = "3.8.5"
    success = 0,
    host.run_expect(success, pyenv(f"pyenv local {version}"))
    yield f"Python {version}"
    assert host.run_expect(success, pyenv("pyenv local --unset"))
    return


def test_python(host, python):
    """ Test the installed Python.

    """
    assert host.check_output(pyenv("python --version")) == python
    return
