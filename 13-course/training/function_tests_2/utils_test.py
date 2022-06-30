# utils_test.py

import pytest

from utils import get_verbal_grade

grade_parameters = [
    (2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично"),
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ("5", TypeError),
    (5.0, TypeError)
]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_verbal_grade(grade_int)
