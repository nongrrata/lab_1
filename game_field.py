from units.unit import Unit
from factories import UnitFactory

class GameFieldIterator:
    def __init__(self, field: "GameField"):
        self._field = field
        self._keys = list(field._units.keys())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._keys):
            raise StopIteration
        key = self._keys[self._index]
        self._index += 1
        return self._field._units[key]

class GameField:
    def __init__(self, width: int, height: int, max_units: int):
        if width <= 0 or width > 50:
            raise ValueError("Недопустимая величина ширины поля")
        self._width = width
        if height <= 0 or height > 30:
            raise ValueError("Недопустимая величина высоты поля")
        self._height = height
        if max_units <= 0 or max_units > width * height // 2:
            raise ValueError("Недопустимое максимальное количество существ")
        self._max_units = max_units
        self._units: dict[tuple[int, int], Unit] = {}

    def deep_copy(self) -> "GameField":
        new_field = GameField(self._width, self._height, self._max_units)
        for pos, unit in self._units.items():
            new_field._units[pos] = unit.clone()
        return new_field

    def add_unit(self, unit: Unit):
        if unit.x <= 0 or unit.x > self._width or unit.y <= 0 or unit.y > self._height:
            raise ValueError("Ошибка (попытка добавить существо вне поля)")
        if len(self._units) >= self._max_units:
            raise ValueError("Достигнуто максимальное количество существ на поле")
        self._units[(unit.x, unit.y)] = unit

    def remove_unit(self, x: int, y: int):
        if (x, y) not in self._units:
            raise ValueError("Ошибка при попытке удаления существа")
        del self._units[(x, y)]

    def get_unit(self, x: int, y: int) -> Unit:
        if (x, y) not in self._units:
            raise ValueError("Ошибка (существо не найдено)")
        return self._units[(x, y)]

    def spawn(self, factory: UnitFactory, kind: str, x: int, y: int) -> Unit:
        unit = factory.create_unit(kind, x, y)
        self.add_unit(unit)
        return unit

    def size(self) -> int:
        return len(self._units)

    def is_empty(self) -> bool:
        return self.size() == 0

    def clear(self):
        self._units.clear()

    def __iter__(self):
        return GameFieldIterator(self)