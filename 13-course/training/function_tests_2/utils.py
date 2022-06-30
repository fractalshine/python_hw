# utils.py

def get_verbal_grade(grade):
    if type(grade) != int:
        raise TypeError("Должно быть целое число между 2 и 5")
    if grade < 2 or grade > 5:
        raise ValueError("Должно быть между 2 и 5")

    if grade == 2:
        return "Плохо"
    elif grade == 3:
        return "Удовлетворительно"
    elif grade == 4:
        return "Хорошо"
    elif grade == 5:
        return "Отлично"
