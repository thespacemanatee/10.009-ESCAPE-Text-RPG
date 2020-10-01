##### MONSTER SETUP #####


class Monster:
    def __init__(self, strength, magic):
        self.strength = strength
        self.magic = magic

    def attack(self):
        return self.strength * self.magic


class Troll(Monster):
    def __init__(self, strength):
        self.name = 'Troll'
        super().__init__(strength=strength * 1.2, magic=strength * 0.5)


class Witch(Monster):
    def __init__(self, magic):
        self.name = 'Witch'
        super().__init__(strength=magic * 0.5, magic=magic * 1.7)