"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, modulo, average


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Expected an error"
    except ZeroDivisionError:
        pass


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(7, 2) == 1


def test_modulo_by_zero():
    try:
        modulo(1, 0)
        assert False, "Expected an error"
    except ValueError:
        pass


def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([10]) == 10.0


def test_average_empty():
    try:
        average([])
        assert False, "Expected an error"
    except ValueError:
        pass
