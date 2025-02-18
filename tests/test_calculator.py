'''My Calculator Test'''
from calculator import Calculator
from faker import Faker

# Initialize Faker for generating random test data
fake = Faker()

def test_addition():
    '''Test that addition function works'''
    a = fake.random_int()
    b = fake.random_int()
    expected = a + b
    assert Calculator.add(a, b) == expected  # Removed 'add' as it's not needed in the method

def test_subtraction():
    '''Test that subtraction function works'''
    a = fake.random_int()
    b = fake.random_int()
    expected = a - b
    assert Calculator.subtract(a, b) == expected

def test_divide():
    '''Test that division function works'''
    a = fake.random_int(min=1, max=100)  # Ensure a is not zero
    b = fake.random_int(min=1, max=100)  # Ensure b is not zero
    expected = a / b
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    '''Test that division by zero raises an error'''
    a = fake.random_int()
    b = 0
    try:
        Calculator.divide(a, b)
    except ZeroDivisionError:
        assert True  # Expected behavior
    else:
        assert False # Fail the test if no exception is raised

def test_multiply():
    '''Test that multiplication function works'''
    a = fake.random_int()
    b = fake.random_int()
    expected = a * b
    assert Calculator.multiply(a, b) == expected