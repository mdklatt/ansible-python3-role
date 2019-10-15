""" Test suite for the Molecule default scenario.

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


@pytest.fixture(scope="module")
def pyenv(host):
    """ Enable the pyenv Python.

    """
    # Can't rely on PATH here because Testinfra seems to be using /bin/sh for
    # execution, so .bash_profile is not being sourced correctly.
    host.run("~/.pyenv/bin/pyenv local 3.6.4")
    return


@pytest.mark.usefixtures("pyenv")
def test_python(host):
    """ Test the installed Python.

    """
    python = "~/.pyenv/shims/python"  # path must be explicit
    assert host.check_output(f"{python:s} --version") == "Python 3.6.4"
    return
