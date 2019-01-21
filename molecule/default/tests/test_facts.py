import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-pxc-1')


def test_local_fact_pxc(host):

    local_facts_file = host.file('/etc/ansible/facts.d/pxc.fact')

    assert local_facts_file.exists
    assert local_facts_file.is_file
    assert local_facts_file.user == 'root'
    assert local_facts_file.group == 'root'
    assert local_facts_file.mode == 0o755

    local_facts = \
        host.ansible("setup")["ansible_facts"]["ansible_local"]["pxc"]

    assert local_facts['wsrep_provider_name'] == "Galera"
