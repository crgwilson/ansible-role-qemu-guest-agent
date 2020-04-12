import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_packages(host):
    p = host.package('qemu-guest-agent')
    assert p.is_installed


def test_default_services(host):
    s = host.service('qemu-guest-agent')
    assert s.is_enabled
    assert not s.is_running
