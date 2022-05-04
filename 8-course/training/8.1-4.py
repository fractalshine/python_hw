class Hero:

    def go_right(self):
        print("Я иду направо")

    def go_left(self):
        print("Я иду налево")

    def observe(self):
        print("Я осматриваюсь")


hero_ = Hero()

hero_.go_left()
hero_.observe()
hero_.go_right()
hero_.go_right()
hero_.go_right()
hero_.observe()
hero_.go_right()

# Я иду налево
# Я осматриваюсь
# Я иду направо
# Я иду направо
# Я иду направо
# Я осматриваюсь
# Я иду направо
