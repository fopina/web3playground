def test_initial_state(accounts):
    """
    how to get funds in test accounts?
    """
    for a in accounts:
        assert a.balance > -1


def test_again():
    assert 1 == 1
