"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["ncats-webd"])
def test_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip_package.get_packages()


@pytest.mark.parametrize("command", ["gunicorn"])
def test_commands(host, command):
    """Test that the expected commands are present."""
    assert host.exists(command)
