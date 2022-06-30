# utils.py
import pytest


def divide(first, second):
    return first / second


# utils_test.py


def test_positive_int():
    assert divide(100, 10) == 10.0


def test_negative_int():
    assert divide(-20, -5) == 4.0


def test_zero_to_int():
    assert divide(0, 2) == 0.0


def test_float():
    assert divide(2.2, 2) == 1.1


def test_type_mismatch():
    with pytest.raises(TypeError):
        divide(True, None)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)
