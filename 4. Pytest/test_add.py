# import modules
import pytest 
from main import add

# function to test add function
def test_addition():
    # test scenarios
    assert add(3, 4) == 7
    assert add(-1, 7) == 6
    assert add(-8, -9) == -17
    assert add(-8, 10) == -18