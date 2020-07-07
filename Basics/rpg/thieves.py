import random

from characters import Character
from attributes import Agile, Sneaky


class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
