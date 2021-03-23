from core import add


def test_add():
    """Check that `add()` works as expected"""
    
    assert add(2, 3) == 5


def test_add_z():
    """Check that `add()` works as expected"""
    
    assert add(2, 3, 1) == 6
