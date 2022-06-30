from utils import get_circle_square
import pytest


def test_get_circle_square_zero():
    square = get_circle_square(0)
    assert square == 0, "Неверное значение для 0"


def test_get_circle_square_one():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14, "Неверное значение для 1"


def test_get_circle_square_normal():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27, "Неверное значение для 3"


def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)


def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")
