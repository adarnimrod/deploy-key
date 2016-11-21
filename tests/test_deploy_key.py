def test_deploy_key(Command, Sudo):
    with Sudo(user='nobody'):
        assert Command('git -C /tmp/ansible-role-deploy-key pull').rc == 0


def test_deply_key_alias(File, Ansible, User):
    assert User('nobody').exists
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'Debian':
        assert File('/etc/aliases').contains('nobody: root')
    elif ansible_os_family == 'OpenBSD':
        assert File('/etc/mail/aliases').contains('nobody: root')
