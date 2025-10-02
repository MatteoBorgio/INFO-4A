from random import randint

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.name = name
        if min_damage < 1:
            raise ValueError("Min damage must be >= 1")
        if max_damage < min_damage:
            raise ValueError("Max damage must be >= min damage")
        if type not in ["melee", "ranged"]:
            raise ValueError("Type must be melee or ranged")
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.type = type
    
    def get_damage(self) -> int:
        return randint(self.min_damage, self.max_damage) 

    def __str__(self):
        return f"The player is {self.name}, with an attack range of ({self.min_damage}, {self.max_damage})"

