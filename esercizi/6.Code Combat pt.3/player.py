from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, health: int, strength: int, dexterity: int, potions: list[Potion]):
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
        self.__buffs = []

    @property
    def buffs(self) -> list[tuple[str,int,int]]:
        return self.__buffs
    
    @property
    def potions(self) -> list[Potion]:
        return self.__potions
    
    @potions.setter
    def potions(self, new_potions: list[Potion]):
        self.__potions = new_potions

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
        effective_strength = self.__strength
        for buff in self.__buffs:
            if buff[0] == "str":
                effective_strength += buff[1]
        return effective_strength
    
    @strength.setter
    def strength(self, value: int) -> None:
        if not 1 <= value <= 20:
            raise ValueError("Strength must be in the range 1–20")
        self.__strength = value

    @property
    def dexterity(self) -> int:
        effective_dexterity = self.__dexterity
        for buff in self.__buffs:
            if buff[0] == "dex":
                effective_dexterity += buff[1]
        return effective_dexterity
    
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
            mod = self.modifier(self.strength)
        else:
            mod = self.modifier(self.dexterity)

        self.__damage += mod
        if self.__damage < 0:
            self.__damage = 0

        enemy.take(self.__damage)
        return self.__damage

    def tick_buffs(self) -> None:
        active_buffs = []
        for buff in self.__buffs:
            new_duration = buff[2] - 1
            if new_duration > 0:
                active_buffs.append((buff[0], buff[1], new_duration))
        self.__buffs = active_buffs

    def use_potion(self, p: Potion) -> dict:
        if p in self.__potions:
            result = p.apply_to(self)
            if "error" in result:
                return result
            self.__potions.remove(p)
            return result
        else:
            print("Can't use the potion")
            return {"error": "potion_not_found"}

    def add_buff(self, stat: str, amount: int, duration: int) -> None:
        if stat not in ["str", "dex"]:
            return {"error": "invalid_buff_type"}
        self.__buffs.append((stat, amount, duration))
        return amount
    
    def heal(self, amount: int) -> int:
        healed = min(amount, self.__max_health - self.__health)
        self.__health += healed
        return healed
    
    def __find_potion(self, potions: list[Potion], researched_effect: str) -> Potion | None:
        for potion in potions:
            if potion.effect == researched_effect and not getattr(potion, "used", False):
                return potion
        return None

    def should_use_potion(self, enemy: "Player") -> Potion | None:
        # 1. Se la salute è critica, cerca una pozione di cura
        potion = self.__find_potion(self.__potions, "heal")
        if self.__health / self.__max_health < 0.3 and potion:
            return potion

        # 2. Buff di forza se nemico forte
        potion = self.__find_potion(self.__potions, "buff_str")
        if enemy.strength > self.__strength + 5 and potion:
            return potion

        # 3. Buff di destrezza se nemico più agile
        potion = self.__find_potion(self.__potions, "buff_dex")
        if enemy.dexterity > self.__dexterity + 5 and potion:
            return potion

        # 4. Buff mancanti
        has_str_buff = any(buff[0] == "str" for buff in self.__buffs)
        has_dex_buff = any(buff[0] == "dex" for buff in self.__buffs)

        if not has_str_buff:
            potion = self.__find_potion(self.__potions, "buff_str")
            if potion:
                return potion
        if not has_dex_buff:
            potion = self.__find_potion(self.__potions, "buff_dex")
            if potion:
                return potion

        # Nessuna pozione da usare
        return None

    def __str__(self) -> str:
        return f"{self.__name}: (HP: {self.__health}/{self.__max_health})"


