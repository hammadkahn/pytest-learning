import pytest


@pytest.fixture()
def setUp():
    """Set up the test fixture before exercising it."""
    print("Launching the browser")
    print("Logging in")
    print("Navigating to the application")


def test_add_to_cart(setUp):
    print("Adding item to cart")


def test_remove_from_cart():
    print("Removing item from cart")
