### Ansible setup

#### Install ssh-pubkey on target host

Generate ssh key pair on with `ssh-keygen` on your local machine.
Recommended encryption is ED25519. (which is more secure than RSA)

```bash
ssh-keygen -t ed25519 -C "pi_cluster"
```

Copy the public key to the target host with `ssh-copy-id`:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host`.
```

#### Ping target host

```bash
ansible myhosts -m ping -i inventory.yaml
```

#### Run playbook

```bash
ansible-playbook -i inventory.yaml playbook.yaml
```
