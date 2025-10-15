from player import Player
from weapon import Weapon
from random import randint

def assign_weapon(player: Player):
    if player.get_strength() > player.get_dexterity():
        player.equip(Weapon("Sword", 5, 10, "melee"))
    else:
        player.equip(Weapon("Bow", 5, 10, "ranged"))

if __name__ == "__main__":
    p1 = Player("Matteo", 50, 50, randint(1, 20), randint(1, 20))
    p2 = Player("Borgio", 50, 50, randint(1, 20), randint(1, 20))
    assign_weapon(p1)
    assign_weapon(p2)
    print("\n=== SIMULAZIONE DI COMBATTIMENTO ===\n")
    print(f"{p1.get_name()}: Forza:{p1.get_strength()}, Destrezza={p1.get_dexterity()}\n")
    print(f"{p2.get_name()}: Forza:{p2.get_strength()}, Destrezza={p2.get_dexterity()}\n")
    print(f"{p1.get_name()} equipaggia: {p1.get_weapon().get_name()} ({p1.get_weapon().get_min_damage()}-{p1.get_weapon().get_max_damage()} dmg)\n")
    print(f"{p2.get_name()} equipaggia: {p2.get_weapon().get_name()} ({p2.get_weapon().get_min_damage()}-{p2.get_weapon().get_max_damage()} dmg)\n")
    print("=== INIZIO COMBATTIMENTO ===\n")
    counter = 0
    while p1.is_alive() and p2.is_alive():
        counter += 1
        print(f"--- TURNO {counter} ---\n")
        print(f"{p1.get_name()} attacca {p2.get_name()} e infligge {p1.attack(p2)} danni!\n")
        print(p2, "\n")
        if p2.is_alive() == False:
            break
        print(f"{p2.get_name()} attacca {p1.get_name()} e infligge {p2.attack(p1)} danni!\n")
        print(p1, "\n")
        if p1.is_alive() == False:
            break
    print("=== COMBATTIMENTO TERMINATO ===\n")
    if p1.is_alive():
        print(f"🏆 {p1.get_name()} vince il combattimento! {p1.get_name()} ({p1.get_health()}/{p1.get_max_health()})\n")
    else:
        print(f"🏆 {p2.get_name()} vince il combattimento! {p2.get_name()} ({p2.get_health()}/{p2.get_max_health()})\n")
        

