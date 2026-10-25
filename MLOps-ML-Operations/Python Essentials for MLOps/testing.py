# Using assertions in a test function 
def test_capitalize():
    assert "hello".capitalize() == "Hello"

# Class with two related test methods
class TestestCalculator:

    def test_add(self):
        calculator = Calculator()
        assert calculator.add(2,2) == 4
    
    def test_multiply(self):
        calculator = Calculator()
        assert calculator.multiply(3,3) == 15

# Test function using pytest fixture for temp data
import pytest

@pytest.fixture
def input_value():
    return 10

def test_stuff(input_value):
    assert input_value == 10

