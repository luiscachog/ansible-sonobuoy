# Ansible Role: Sonobuoy

[![Build Status](https://travis-ci.com/k4ch0/ansible-sonobuoy.svg?branch=master)](https://travis-ci.com/k4ch0/ansible-sonobuoy)
[![Actions Status](https://github.com/k4ch0/ansible-sonobuoy/workflows/Molecule%20Test/badge.svg)](https://github.com/k4ch0/ansible-sonobuoy/actions)
[![codecov](https://codecov.io/gh/k4ch0/ansible-sonobuoy/branch/master/graph/badge.svg)](https://codecov.io/gh/k4ch0/ansible-sonobuoy)

Ansible role that installs [VMware-Tanzy Sonobuoy](https://github.com/vmware-tanzu/sonobuoy), a diagnostic tool that makes it easier to understand the state of a Kubernetes cluster. 

## Requirements

None

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

  sonobuoy_version: "0.17.0"

The Sonobuoy version to install.

  sonobuoy_arch: "amd64"

The system architecture (e.g. `386` or `amd64`) to use.

  sonobuoy_install_dir: /usr/local/bin

The location where the Sonobuoy binary will be installed (should be in system `$PATH`).

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - k4ch0.sonobuoy
```

## License

MIT

## Author Information

This role was created on May 2019 by [Luis Cacho](https://luiscachog.io)