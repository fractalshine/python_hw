from class_tests.ticket_utils import ticket_price


class TestTicketPrice:

    def test__0__test(self):
        assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"

    def test__1__test(self):
        assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"

    def test_7(self):
        assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"

    def test_18(self):
        assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"

    def test_25(self):
        assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"

    def test_60(self):
        assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"

    def test_minus_1(self):
        assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"
