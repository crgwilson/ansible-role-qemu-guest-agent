# Ansible role: qemu-guest-agent

![Molecule Test](https://github.com/crgwilson/ansible-role-qemu-guest-agent/workflows/Molecule%20Test/badge.svg)

Install and manage the [qemu-guest-agent](https://wiki.libvirt.org/page/Qemu_guest_agent)


## Variables

All variables are really straight forward, there's no real reason to need to change any of them.


## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
