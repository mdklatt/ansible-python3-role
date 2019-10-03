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


@pytest.mark.parametrize("cmd", ("python3.6", "python3", "pip3", "virtualenv"))
def test_commands(host, cmd):
    """ Test for installed Python commands.

    """
    # FIXME: `pipenv` fails due to missing environment variables.
    # FIXME: Fails when running as root: no pyenv installation found
    for command in ("pyenv local 3.6.4", f"{cmd:s} --version"):
        assert host.command(command).rc == 0
    return
