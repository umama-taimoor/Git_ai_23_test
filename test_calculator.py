import pytest

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 7, -6),
    (-5, -1, -4),
    (0, 0, 0)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (4, 3, 12),
    (-1, 7, -7),
    (2.0, 3.0, 6.0),
    (-5.0, -5.0, 25.0),
    (0, 6, 0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    result = calculator.multiply(a, b)
    assert abs(result - expected) < 0.0001, f"Expected {expected} but got {result}"

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (12, 3, 4),
    (7.5, 2.5, 3.0)
])
def test_divide_parameterized(calculator, a, b, expected):
    result = calculator.divide(a, b)
    assert abs(result - expected) < 0.0001, f"Expected {expected} but got {result}"

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(7, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),  # Should be 1/(2^2) = 0.25
    (10, -1, 0.1)   # Should be 1/10 = 0.1
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),   
    (1, 1),   
    (4, 24),  
    (5, 120)   
])
def test_factorial_parameterized(calculator, n, expected):
    assert calculator.factorial(n) == expected

def test_factorial_negative(calculator):
    with pytest.raises(ValueError):
        calculator.factorial(-5)

@pytest.mark.parametrize("n, expected", [
    (0, 0),   
    (1, 1),    
    (2, 1),   
    (3, 2),    
    (5, 5),    
    (7, 13)    
])
def test_fibonacci_parameterized(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

def test_fibonacci_negative(calculator):
    with pytest.raises(ValueError):
        calculator.fibonacci(-3)
def test_precise_multiplication(precise_calculator):
    result = precise_calculator.multiply(1.304, 3.235)
    assert result == 4.22
def test_different_precisions(precise_calculator):
    result = precise_calculator.add(1.304, 3.235)
    
    if precise_calculator.precision == 1:
        assert result == 4.5
    elif precise_calculator.precision == 2:
        assert result == 4.54
    elif precise_calculator.precision == 3:
        assert result == 4.539


