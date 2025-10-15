from random import randint

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.__name = name
        if min_damage < 1:
            raise ValueError("Min damage must be >= 1")
        if max_damage < min_damage:
            raise ValueError("Max damage must be >= min damage")
        if type not in ["melee", "ranged"]:
            raise ValueError("Type must be melee or ranged")
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__type = type

    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str) -> None:
        if name != "" and name is not None:
            self.__name = name
        else:
            print("\nValore non valido\n")

    def get_min_damage(self) -> int:
        return self.__min_damage
    
    def set_min_damage(self, min_damage: int) -> None:
        if min_damage <= self.__max_damage:
            self.__min_damage = min_damage
        else:
            print("\nValore non valido\n")
    
    def get_max_damage(self) -> int:
        return self.__max_damage
    
    def set_min_damage(self, max_damage: int) -> None:
        if max_damage >= self.__min_damage:
            self.__max_damage = max_damage
        else:
            print("\nValore non valido\n")

    def get_type(self) -> str:
        return self.__type
    
    def set_type(self, type: str):
        if type in ["melee", "ranged"]:
            self.__type = type
        else:
            print("\nValore non valido\n")
    
    def get_damage(self) -> int:
        return randint(self.__min_damage, self.__max_damage) 

    def __str__(self):
        return f"The player is {self.__name}, with an attack range of ({self.__min_damage}, {self.__max_damage})"

