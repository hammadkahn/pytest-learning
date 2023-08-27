import pytest


def test_login():
    print("Login Successfull")


def test_logout():
    print("Logout Successfull")


@pytest.mark.sanity
def testcalc():
    assert 100 + 200 == 3001
