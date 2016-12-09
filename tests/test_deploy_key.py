from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_deploy_key(Command, Sudo):
    with Sudo(user='nobody'):
        assert Command('git -C /tmp/ansible-role-deploy-key pull').rc == 0


def test_deply_key_alias(File, User, SystemInfo):
    assert User('nobody').exists
    if SystemInfo.type == 'linux':
        assert File('/etc/aliases').contains('nobody: root')
    elif SystemInfo.type == 'openbsd':
        assert File('/etc/mail/aliases').contains('nobody: root')
