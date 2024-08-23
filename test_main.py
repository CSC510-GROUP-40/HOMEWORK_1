import pytest
from main import solve_quadratic 

def test_solve_quadratic_passing():
    # Test the equation x^2 - 3x + 2 = 0
    result = solve_quadratic(1, -3, 2)
    expected = (2.0, 1.0)
    assert result == expected, f"Expected {expected}, but got {result}"


#def test_solve_quadratic_failing():
    # Test the equation 2x^2 + 4x - 6 = 0 with an incorrect expected value
#    result = solve_quadratic(2, 4, -6)
#    expected = (2.0, -2.0)  # Incorrect expected value
#    assert result == expected, f"Expected {expected}, but got {result}"


def test_solve_quadratic_zero_discriminant():
    # Test the equation x^2 - 4x + 4 = 0
    result = solve_quadratic(1, -4, 4)
    expected = 2.0  # Since it's a repeated root
    assert result == expected, f"Expected {expected}, but got {result}"


def test_solve_quadratic_complex_roots():
    # Test the equation x^2 + 2x + 5 = 0
    result = solve_quadratic(1, 2, 5)
    expected =  "complex roots"
    assert result == expected, f"Expected {expected}, but got {result}"
