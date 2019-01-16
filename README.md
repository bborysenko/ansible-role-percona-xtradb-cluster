<p><img src="https://cdn.worldvectorlogo.com/logos/percona.svg" alt="percona logo" title="percona" align="right" height="60" /></p>

ansible-role-percona-xtradb-cluster
===================================

[![Build Status](https://travis-ci.org/bborysenko/ansible-role-percona-xtradb-cluster.svg?branch=master)](https://travis-ci.org/bborysenko/ansible-role-percona-xtradb-cluster)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-bborysenko.percona--xtradb--cluster-blue.svg)](https://galaxy.ansible.com/bborysenko/percona-xtradb-cluster/)
[![GitHub tag](https://img.shields.io/github/tag/bborysenko/ansible-role-percona-xtradb-cluster.svg)](https://github.com/bborysenko/ansible-role-percona-xtradb-cluster/tags)

Ansible role to deploy Percona XtraDB Cluster.

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

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: percona-xtradb-cluster, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
