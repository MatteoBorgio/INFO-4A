from weapon import Weapon

class Player:
    def __init__(self, name: str, max_health: int, health: int, strength: int, dexterity: int):
        if max_health < 1:
            raise ValueError("Max health must be >= 1")
        if health != max_health:
            raise ValueError("Health must be == to max_health")
        if strength < 1 or strength > 20:
            raise ValueError("Strength value must be in a (1-20) range")
        if dexterity < 1 or dexterity > 20:
            raise ValueError("Dexterity range must be in a (1-20) range")
        self.__name = name
        self.__max_health = max_health
        self.__health = health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__weapon = None 
        self.__damage = 0
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str) -> None:
        if name != "" and name is not None:
            self.__name = name
        else:
            print("\nValore non valido\n")
    
    def get_max_health(self) -> int:
        return self.__max_health
    
    def set_max_health(self, max_health: int) -> None:
        if max_health > 0 and max_health >= self.__health:
            self.__max_health = max_health
        else:
            print("\nValore non valido\n")

    def get_health(self) -> int:
        return self.__health
    
    def set_health(self, health: int) -> None:
        if health >= 0 and health <= self.__max_health:
            self.__health = health
        else:
            print("\nValore non valido\n")

    def get_strength(self) -> int:
            return self.__strength
    
    def set_strength(self, strength: int) -> None:
        if strength >= 1 and strength <= 20:
            self.__strength = strength
        else:
            print("\nValore non valido\n")

    def get_dexterity(self) -> int:
        return self.__dexterity
    
    def set_dexterity(self, dexterity: int) -> None:
        if dexterity >= 1 and dexterity <= 20:
            self.__dexterity = dexterity
        else:
            print("\nValore non valido\n")

    def get_weapon(self) -> Weapon:
        return self.__weapon
    
    def set_weapon(self, weapon: Weapon) -> None:
        if type(weapon) == Weapon:
            self.__weapon = weapon
        else:
            print("\nValore non valido\n")
        
    def equip(self, weapon: Weapon) -> None:
        if type(weapon) == Weapon:
            self.__weapon = weapon
        else:
            ("\nL'oggetto che stai cercando di equipaggiare non è un'arma valida\n")

    def modifier(self, value: int) -> int:
        return ((value - 10) // 2)
    
    def is_alive(self) -> bool:
        if self.__health > 0:
            return True
        else:
            return False
        
    def take(self, damage: int) -> int:
        initial_health = self.__health
        if damage >= self.__health:
            self.__health = 0
            return initial_health
        else:
            self.__health -= damage
            return damage

    def attack(self, enemy: "Player") -> int:
        if self.__weapon == None:
            self.__damage = 1
            return enemy.take(self.__damage)
        self.__damage = self.__weapon.get_damage()
        if self.__weapon.get_type() == "melee":
            mod = self.modifier(self.__strength)
        else:
            mod = self.modifier(self.__dexterity)
        self.__damage += mod
        if self.__damage < 0:
            self.__damage = 0
        enemy.take(self.__damage)
        return self.__damage
    
    def __str__(self):
        return f"{self.__name}: (HP: {self.__health}/{self.__max_health})"