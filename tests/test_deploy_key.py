from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_deploy_key(Command, Sudo):
    with Sudo(user='nobody'):
        assert Command(
            'git --git-dir /tmp/ansible-role-deploy-key/.git pull').rc == 0


def test_deploy_key_root(Command, Sudo):
    with Sudo():
        assert Command(
            'git --git-dir /tmp/ansible-role-deploy-key/.git pull').rc == 0
