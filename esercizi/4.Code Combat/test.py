from player import Player
from weapon import Weapon
from random import randint

def assign_weapon(player: Player):
    if player.strength > player.dexterity:
        player.equip(Weapon("Sword", 5, 10, "melee"))
    else:
        player.equip(Weapon("Bow", 5, 10, "ranged"))

if __name__ == "__main__":
    p1 = Player("Matteo", 20, 20, randint(1, 20), randint(1, 20))
    p2 = Player("Borgio", 20, 20, randint(1, 20), randint(1, 20))
    assign_weapon(p1)
    assign_weapon(p2)
    print("=== SIMULAZIONE DI COMBATTIMENTO ===\n")
    print(f"{p1.name}: Forza:{p1.strength}, Destrezza={p1.dexterity}\n")
    print(f"{p2.name}: Forza:{p2.strength}, Destrezza={p2.dexterity}\n")
    print(f"{p1.name} equipaggia: {p1.weapon.name} ({p1.weapon.min_damage}-{p1.weapon.max_damage} dmg)\n")
    print(f"{p2.name} equipaggia: {p2.weapon.name} ({p2.weapon.min_damage}-{p2.weapon.max_damage} dmg)\n")
    print("=== INIZIO COMBATTIMENTO ===")
    counter = 0
    while p1.is_alive() and p2.is_alive():
        counter += 1
        print(f"\n--- TURNO {counter} ---\n")
        p1.attack(p2)
        p2.attack(p1)
        

