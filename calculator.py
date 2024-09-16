import math

def sqrt(x):
    """Square Root"""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return math.sqrt(x)


# calculator.py
def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
