from abc import ABC, abstractmethod
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack

class Unit(ABC):
    def __init__(self, health: Health, armor: Armor, attack: Attack, x: int, y: int):
        self._health = health
        self._armor = armor
        self._attack = attack
        self._x = x
        self._y = y

    @property
    def health(self): return self._health.value

    @property
    def armor(self): return self._armor.value

    @property
    def attack(self): return self._attack.value

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @abstractmethod
    def clone(self) -> "Unit":
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

    def move(self, new_x: int, new_y: int):
        self._x = new_x
        self._y = new_y

    def take_damage(self, amount: int):
        self._health.decrease(self._armor.reduce_damage(amount))

    def is_alive(self) -> bool:
        return not self._health.is_zero()