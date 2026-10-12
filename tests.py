from factories import InfantryFactory
from game_field import GameField
from units.infantry import Swordsman
from attributes.health import Health
from attributes.armor import Armor
from attributes.attack import Attack

def test_create_field_via_factory():
    factory = InfantryFactory()
    field = GameField(10, 10, 50)

    unit = factory.create_unit("swordsman", 1, 1)
    field.add_unit(unit)

    assert field.size() == 1, "Существо не добавилось"
    assert field.get_unit(1, 1) is unit, "Существо лежит не там"
    print("✅ Сценарий 1: создание через фабрику")

def test_deep_copy_independence():
    field = GameField(10, 10, 50)
    field.add_unit(Swordsman(Health(100), Armor(20), Attack(15), 1, 1))

    copy = field.deep_copy()

    assert copy.size() == field.size(), "Размер копии не совпал"

    orig_unit = field.get_unit(1, 1)
    copy_unit = copy.get_unit(1, 1)
    assert orig_unit is not copy_unit, "Копия ссылается на тот же объект"

    copy_unit.take_damage(50)
    assert orig_unit._health.value == 100, "Оригинал изменился вместе с копией"
    assert copy_unit._health.value == 70, "Копия не получила урон"

    print("✅ Сценарий 2: глубокое копирование независимо")

def test_iteration_mass_action():
    field = GameField(10, 10, 50)
    for i in range(1, 6, 1):
        field.add_unit(Swordsman(Health(100), Armor(20), Attack(15), i, 1))

    count = 0
    for unit in field:
        unit.take_damage(30)
        count += 1

    assert count == 5, f"Обошли {count} существ вместо 5"
    for unit in field:
        assert unit._health.value == 90, "Урон применился не ко всем"

    print("✅ Сценарий 4: массовое действие через итератор")

def run_all_tests():
    test_create_field_via_factory()
    test_deep_copy_independence()
    test_iteration_mass_action()