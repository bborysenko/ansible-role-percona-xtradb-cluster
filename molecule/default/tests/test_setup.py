import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-pxc-1')


def test_mysql_is_installed(host):
    packages = {
        'Percona-XtraDB-Cluster-57': '5.7',
        'percona-toolkit': '3.0',
        'percona-xtrabackup-24': '2.4'
    }

    for package, version in packages.items():
        pkg = host.package(package)
        assert pkg.is_installed
        assert pkg.version.startswith(version)


def test_mysql_running_and_enabled(host):
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled
