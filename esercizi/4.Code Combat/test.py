from player import Player
from weapon import Weapon
from random import randint

def assign_weapon(player: Player):
    if player.strength > player.dexterity:
        player.equip(Weapon("Sword", 5, 10, "melee"))
    else:
        player.equip(Weapon("Bow", 5, 10, "ranged"))

if __name__ == "__main__":
    p1 = Player("Matteo", 50, 50, randint(1, 20), randint(1, 20))
    p2 = Player("Borgio", 50, 50, randint(1, 20), randint(1, 20))
    assign_weapon(p1)
    assign_weapon(p2)
    print("\n=== SIMULAZIONE DI COMBATTIMENTO ===\n")
    print(f"{p1.name}: Forza:{p1.strength}, Destrezza={p1.dexterity}\n")
    print(f"{p2.name}: Forza:{p2.strength}, Destrezza={p2.dexterity}\n")
    print(f"{p1.name} equipaggia: {p1.weapon.name} ({p1.weapon.min_damage}-{p1.weapon.max_damage} dmg)\n")
    print(f"{p2.name} equipaggia: {p2.weapon.name} ({p2.weapon.min_damage}-{p2.weapon.max_damage} dmg)\n")
    print("=== INIZIO COMBATTIMENTO ===\n")
    counter = 0
    while p1.is_alive() and p2.is_alive():
        counter += 1
        print(f"--- TURNO {counter} ---\n")
        print(f"{p1.name} attacca {p2.name} e infligge {p1.attack(p2)} danni!\n")
        print(f"{p2.name} (HP: {p2.health}/{p2.max_health})\n")
        if p2.is_alive() == False:
            break
        print(f"{p2.name} attacca {p1.name} e infligge {p2.attack(p1)} danni!\n")
        print(f"{p1.name} (HP: {p1.health}/{p1.max_health})\n")
        if p1.is_alive() == False:
            break
    print("=== COMBATTIMENTO TERMINATO ===\n")
    if p1.is_alive():
        print(f"🏆 {p1.name} vince il combattimento! {p1.name} ({p1.health}/{p1.max_health})\n")
    else:
        print(f"🏆 {p2.name} vince il combattimento! {p2.name} ({p2.health}/{p2.max_health})\n")
        

