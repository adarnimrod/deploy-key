def test_deploy_key(Command, Sudo):
    with Sudo(user='nobody'):
        assert Command('git -C /tmp/ansible-role-deploy-key pull').rc == 0
