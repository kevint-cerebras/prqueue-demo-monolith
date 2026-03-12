"""Simple calculator module used by the kernel test harness."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
