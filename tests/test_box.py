def test_initial_state(accounts):
    """
    how to get funds in test accounts?
    """
    for a in accounts:
        assert a.balance == 1000000000000000000000000


def test_box(owner, project, accounts):
    deployment = owner.deploy(project.Box)
    assert deployment.retrieve() == 0
    deployment.store(2, sender=accounts[1])
    assert deployment.retrieve(sender=owner) == 2


def test_proxied_box(owner, project, accounts):
    deployment = owner.deploy(project.BoxProxy)
    assert deployment.retrieve() == 0
    deployment.store(2, sender=accounts[1])
    assert deployment.retrieve(sender=owner) == 2
