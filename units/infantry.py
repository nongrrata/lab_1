from abc import ABC, abstractmethod
from units.unit import Unit
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack

class Infantry(Unit, ABC):
    pass

class Swordsman(Infantry):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self) -> "Swordsman":
        return Swordsman(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self) -> str:
        return "Swordsman"

    def _symbol(self) -> str:
        return "SW"

class Spearman(Infantry):
    def __init__(self, health, armor, attack, x, y):
        super().__init__(health, armor, attack, x, y)
    def clone(self) -> "Spearman":
        return Spearman(
            Health(self._health.value),
            Armor(self._armor.value),
            Attack(self._attack.value),
            self._x,
            self._y
        )

    def get_type(self) -> str:
        return "Spearman"

    def _symbol(self) -> str:
        return "SP"