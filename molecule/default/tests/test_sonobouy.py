import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sonobuoy_file(host):
    file = host.file("/usr/local/bin/sonobuoy")

    assert file.exists
    assert file.is_symlink


def test_sonobuoy_binary(host):
    binary = host.find_command('sonobuoy')

    assert binary
