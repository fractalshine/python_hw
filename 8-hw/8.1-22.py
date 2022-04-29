# Создай класс Number c полем value (указывается при инициализации)
#
# Создай экземпляр, например
# x = Number(7)
#
# Добавь методы:
#
# .get()
#  возвращает текущее value
#
# .add(<значение>)
#  добавляет указанное число к value
#
# .subtract(<значение>)
#  вычитает указанное число из value

class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, number):
        self.value += number

    def subtract(self, number):
        self.value -= number


# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())
