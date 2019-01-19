import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-pxc-1')


def test_root_is_able_to_connect_to_mysql_without_password(host):
    r = host.run("mysql -e 'SHOW DATABASES'")
    assert r.rc == 0
    assert "mysql" in r.stdout
