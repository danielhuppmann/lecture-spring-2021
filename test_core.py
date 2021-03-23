from core import *


def test_add():
    """Check that `add()` works as expected"""

    assert add(2, 3) == 5


def test_add_z():
    """Check that `add()` works as expected"""

    assert add(2, 3, 1) == 6


def test_add_2():
    """Check that `add()` works as expected"""

    assert add_2(3) == 5