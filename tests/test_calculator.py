'''My Calculator Test'''
from calculator import Calculator, Calculation

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(2, 2) == 4
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(0, 1) == -1

def test_multiplication():
    '''Test that multiplication function works'''
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.multiply(2, -2) == -4
    assert Calculator.multiply(0, 5) == 0

def test_division():
    '''Test that division function works'''
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(10, 5) == 2
    assert Calculator.divide(1, -1) == -1

def test_division_by_zero():
    '''Test that division by zero raises an error'''
    try:
        Calculator.divide(5, 0)
        assert False  # If this runs, the test should fail
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_calculation():
    '''Test the Calculation class'''
    calc = Calculation(Calculator.add, 2, 3)
    assert calc.result == 5

    calc2 = Calculation(Calculator.multiply, 4, 5)
    assert calc2.result == 20

def test_calculator_history():
    '''Test calculator history functionality'''
    Calculator.clear_history()  # Start with an empty history

    Calculator.perform_operation(Calculator.add, 1, 1)
    Calculator.perform_operation(Calculator.subtract, 5, 3)

    history = Calculator.get_history()
    assert len(history) == 2
    assert history[0] == "1 add 1 = 2"
    assert history[1] == "5 subtract 3 = 2"

    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0  # Ensure history is cleared
