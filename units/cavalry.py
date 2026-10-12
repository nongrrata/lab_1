from abc import ABC, abstractmethod
from units.unit import Unit
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack

class Cavalry(Unit, ABC):
    pass

class Cataphract(Cavalry):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self):
        return Cataphract(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self):
        return "Cataphract"

class HorseArcher(Cavalry):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self):
        return HorseArcher(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self):
        return "HorseArcher"