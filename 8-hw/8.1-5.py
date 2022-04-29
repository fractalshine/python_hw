class Hero:

    def go_right(self, meters):
        print(f"Я иду {meters} метров направо")

    def go_left(self, meters):
        print(f"Я иду {meters} метров налево")

    def observe(self):
        print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()
