<p><img src="https://cdn.worldvectorlogo.com/logos/percona.svg" alt="percona logo" title="percona" align="right" height="60" /></p>

Ansible Role: Percona XtraDB Cluster
====================================

[![Build Status](https://travis-ci.org/bborysenko/ansible_role_percona_xtradb_cluster.svg?branch=master)](https://travis-ci.org/bborysenko/ansible_role_percona_xtradb_cluster)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
![Ansible Galaxy](https://img.shields.io/ansible/role/36320.svg)
![Downloads](https://img.shields.io/ansible/role/d/36320.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F36320%2F&query=$.min_ansible_version)
[![GitHub tag](https://img.shields.io/github/tag/bborysenko/ansible_role_percona_xtradb_cluster.svg)](https://github.com/bborysenko/ansible_role_percona_xtradb_cluster/tags)

Ansible role to manage Percona XtraDB Cluster on RHEL/CentOS 7.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

```
- name: Percona XtraDB Cluster
  hosts: pxc
  roles:
    - role: bborysenko.percona-xtradb-cluster
      pxc_root_password: Super_P@s$0rd
```

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
