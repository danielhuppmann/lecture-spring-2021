from core import add
from core import sub


def test_add():
    """Check that `add()` works as expected"""
    
    assert add(2, 3) == 5


def test_add_z():
    """Check that `add()` works as expected"""
    
    assert add(2, 3, 1) == 6
    
def test_sub():
    """Check that `sub()` works as expected"""
    
    assert sub(3, 1) == 2
