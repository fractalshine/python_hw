class Hero:

    def __init__(self, name):
        self.name = name
        self.things = []

    def collect(self, thing):
        self.things.append(thing)


# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир")
pythomir.collect("Усы хитрости")
pythomir.collect("Рукавички пряморукости")

if len(pythomir.things) == 2:
    print("Проверка пройдена")
else:
    print("Добавление в список things работает некорректно")

print(pythomir.name)
