from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_deploy_key(Command, Sudo):
    with Sudo(user='nobody'):
        assert Command('git -C /tmp/ansible-role-deploy-key pull').rc == 0
