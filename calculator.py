"""Simple calculator module used by the kernel test harness."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
