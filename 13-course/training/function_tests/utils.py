import math


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Должно быть int или float больше 0")

    if radius < 0:
        raise ValueError("Должно быть int или float больше 0")

    return radius ** 2 * math.pi
