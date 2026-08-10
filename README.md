# ansible-role-ncats-webd #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-ncats-webd/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-ncats-webd/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-ncats-webd)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-ncats-webd/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-ncats-webd/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/ncats-webd](https://github.com/cisagov/ncats-webd).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
| -------- | ----------- | ------- | -------- |
| ncats\_webd\_cyhy\_core\_version | The version of cisagov/cyhy-core to use; must be a valid git reference. | `v1.3.2` | No |
| ncats\_webd\_install\_geoipupdate | Whether to install the MaxMind geoipupdate tool. | `false` | No |
| ncats\_webd\_maxmind\_account\_id | The MaxMind account ID for access to a GeoIP2 database subscription. | n/a | Yes |
| ncats\_webd\_maxmind\_license\_key | The MaxMind license key that provided access to a GeoIP2 database subscription. | n/a | Yes |
| ncats\_webd\_version | The version of cisagov/ncats-webd to install; must be a valid git reference. | `v1.0.1` | No |

## Dependencies ##

- [cisagov/ansible-role-cyhy-core](https://github.com/cisagov/ansible-role-cyhy-core)
- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: ncats_webd
  src: https://github.com/cisagov/ansible-role-ncats-webd
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install cisagov/ncats-webd
      ansible.builtin.include_role:
        name: ncats_webd
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
