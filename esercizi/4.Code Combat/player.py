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
        self.name = name
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.weapon = None 
        self.damage = 0
    
    def equip(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def modifier(self, value: int) -> int:
        return ((value - 10) // 2)
    
    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False
        
    def take(self, damage: int):
        initial_health = self.health
        if damage >= self.health:
            self.health = 0
            return initial_health
        else:
            self.health -= damage
            return damage


    def attack(self, enemy: "Player") -> int:
        if self.weapon == None:
            self.damage = 1
            return enemy.take(self.damage)
        self.damage = self.weapon.get_damage()
        if self.weapon.type == "melee":
            mod = self.modifier(self.strength)
        else:
            mod = self.modifier(self.dexterity)
        self.damage += mod
        if self.damage < 0:
            self.damage = 0
        enemy.take(self.damage)
        return self.damage
    
    def __str__(self):
        return f"{self.name}: (HP: {self.health}/{self.max_health})"

