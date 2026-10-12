from abc import ABC, abstractmethod
from units.unit import Unit
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack

class Archer(Unit, ABC):
    pass

class LightArcher(Archer):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self) -> "LightArcher":
        return LightArcher(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self):
        return "LightArcher"

class HeavyArcher(Archer):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self) -> "HeavyArcher":
        return HeavyArcher(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self):
        return "HeavyArcher"