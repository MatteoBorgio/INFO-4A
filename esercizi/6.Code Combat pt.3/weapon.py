from random import randint

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.__name = name
        if min_damage < 1:
            raise ValueError("Min damage must be >= 1")
        if max_damage < min_damage:
            raise ValueError("Max damage must be >= min damage")
        if type not in ["melee", "ranged"]:
            raise ValueError("Type must be 'melee' or 'ranged'")

        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value and isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def min_damage(self) -> int:
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, value: int) -> None:
        if value < 1:
            raise ValueError("Min damage must be >= 1")
        if value > self.__max_damage:
            raise ValueError("Min damage must be <= max damage")
        self.__min_damage = value

    @property
    def max_damage(self) -> int:
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value: int) -> None:
        if value < self.__min_damage:
            raise ValueError("Max damage must be >= min damage")
        self.__max_damage = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        if value not in ["melee", "ranged"]:
            raise ValueError("Type must be 'melee' or 'ranged'")
        self.__type = value

    def get_damage(self) -> int:
        return randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"{self.__name} (Type: {self.__type}, Damage: {self.__min_damage}-{self.__max_damage})"
