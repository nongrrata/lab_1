from abc import ABC, abstractmethod
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack
from units.unit import Unit
from units.infantry import Swordsman, Spearman
from units.archer import LightArcher, HeavyArcher
from units.cavalry import Cataphract, HorseArcher

class UnitFactory(ABC):
    @abstractmethod
    def create_unit(self, kind: str, x: int, y: int) -> Unit:
        pass

class InfantryFactory(UnitFactory):
    def create_unit(self, kind: str, x: int, y: int) -> Unit:
        if kind == "swordsman":
            return Swordsman(Health(100), Armor(20), Attack(15), x, y)
        elif kind == "spearman":
            return Spearman(Health(50), Armor(10), Attack(25), x, y)
        else:
            raise ValueError(f"Неизвестный тип пехоты: {kind}")

class ArcherFactory(UnitFactory):
    def create_unit(self, kind: str, x: int, y: int) -> Unit:
        if kind == "light_archer":
            return LightArcher(Health(75), Armor(5), Attack(20), x, y)
        elif kind == "heavy_archer":
            return HeavyArcher(Health(100), Armor(15), Attack(20), x, y)
        else:
            raise ValueError(f"Неизвестный тип стрелка: {kind}")

class CavalryFactory(UnitFactory):
    def create_unit(self, kind: str, x: int, y: int) -> Unit:
        if kind == "cataphract":
            return Cataphract(Health(75), Armor(25), Attack(20), x, y)
        elif kind == "horse_archer":
            return HorseArcher(Health(65), Armor(15), Attack(25), x, y)
        else:
            raise ValueError(f"Неизвестный тип кавалерии: {kind}")