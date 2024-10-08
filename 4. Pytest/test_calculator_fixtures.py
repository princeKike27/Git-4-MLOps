import pytest 
from calculator import add, substract

# Setup
@pytest.fixture
def calculator_setup():
    print('Setting up the environment for Calculator ...')
    return {} 


def test_add(calculator_setup):
    assert add(3, 4) == 7


def test_substract(calculator_setup):
    assert substract(7, 9) == -2