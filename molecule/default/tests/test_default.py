"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkg",
    [
        "gunicorn",
        "python-cffi",
        "python-dateutil",
        "python-docopt",
        "python-flask",
        "python-gevent",
        "python-greenlet",
        "python-gunicorn",
        "python-netaddr",
        "python-schedule",
    ],
)
def test_apt_packages(host, pkg):
    """Test that the apt packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg_name,pkg_version", [("ncats-webd", "1.0.1")])
def test_pip_packages(host, pkg_name, pkg_version):
    """Test that the pip packages were installed."""
    pip_packages = host.pip.get_packages(pip_path="/usr/bin/pip2")

    assert pkg_name in pip_packages
    assert pip_packages[pkg_name]["version"] == pkg_version


@pytest.mark.parametrize("command", ["gunicorn"])
def test_commands(host, command):
    """Test that the expected commands are present."""
    assert host.exists(command)
