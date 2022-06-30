import pytest

from ticket_utils import ticket_price


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, "Бесплатно"),
     (1, "Бесплатно"),
     (7, "100 рублей")]
)
def test_one(test_input, expected):
    assert ticket_price(test_input) == expected
