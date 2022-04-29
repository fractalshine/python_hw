class Hero():

    def __init__(self, name, possessions):
        self.name = name
        self.possessions = possessions

    def __repr__(self):
        return f"Герой {self.name} взял с собой {', '.join(self.possessions)}"


hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
print(hero)
