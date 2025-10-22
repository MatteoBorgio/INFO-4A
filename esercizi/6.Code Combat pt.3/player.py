from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, health: int, strength: int, dexterity: int, buffs: list[tuple[str,int,int]], potions: list[Potion]):
        if max_health < 1:
            raise ValueError("Max health must be >= 1")
        if health != max_health:
            raise ValueError("Health must be == to max_health")
        if strength < 1 or strength > 20:
            raise ValueError("Strength value must be in the range 1–20")
        if dexterity < 1 or dexterity > 20:
            raise ValueError("Dexterity value must be in the range 1–20")
        if len(potions) > 3:
            raise ValueError("The player can't equip more than 3 potions")
        
        self.__potions = potions
        self.__name = name
        self.__max_health = max_health
        self.__health = health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__weapon = None
        self.__damage = 0
        self.__buffs = buffs

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Name can't be empty.")
        self.__name = new_name

    @property
    def max_health(self) -> int:
        return self.__max_health

    @max_health.setter
    def max_health(self, new_max_health: int) -> None:
        if new_max_health <= 0:
            raise ValueError("Max health must be > 0")
        if new_max_health < self.__health:
            raise ValueError("Max health can't be < current health")
        self.__max_health = new_max_health

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, new_health: int) -> None:
        if new_health > self.__max_health:
            raise ValueError("Health must be <= max_health")
        if new_health < 0:
            raise ValueError("Health must be >= 0")
        self.__health = new_health

    @property
    def strength(self) -> int:
        return self.__strength

    @strength.setter
    def strength(self, value: int) -> None:
        if not 1 <= value <= 20:
            raise ValueError("Strength must be in the range 1–20")
        self.__strength = value

    @property
    def dexterity(self) -> int:
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, value: int) -> None:
        if not 1 <= value <= 20:
            raise ValueError("Dexterity must be in the range 1–20")
        self.__dexterity = value

    @property
    def weapon(self) -> Weapon:
        return self.__weapon
    
    @weapon.setter
    def weapon(self, value: Weapon) -> None:
        if not isinstance(value, Weapon):
            raise ValueError("The equipped item must be a Weapon instance.")
        self.__weapon = value

    def modifier(self, value: int) -> int:
        return (value - 10) // 2

    def is_alive(self) -> bool:
        return self.__health > 0

    def take(self, damage: int) -> int:
        initial_health = self.__health
        if damage >= self.__health:
            self.__health = 0
            return initial_health
        else:
            self.__health -= damage
            return damage

    def attack(self, enemy: "Player") -> int:
        if self.__weapon is None:
            self.__damage = 1
            return enemy.take(self.__damage)

        self.__damage = self.__weapon.get_damage()

        if self.__weapon.type == "melee":
            mod = self.modifier(self.__strength)
        else:
            mod = self.modifier(self.__dexterity)

        self.__damage += mod
        if self.__damage < 0:
            self.__damage = 0

        enemy.take(self.__damage)
        return self.__damage

    def __str__(self) -> str:
        return f"{self.__name}: (HP: {self.__health}/{self.__max_health})"

