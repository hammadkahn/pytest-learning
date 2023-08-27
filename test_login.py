import pytest


def testlogin():
    print("Login Successfull")


def testlogout():
    print("Logout Successfull")


@pytest.mark.sanity
def testcalc():
    assert 100 + 200 == 3001
