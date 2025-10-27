from player import Player
from weapon import Weapon
from potion import Potion
from random import randint

def assign_weapon(player: Player) -> None:
    if player.strength > player.dexterity:
        player.weapon = Weapon("Sword", 5, 10, "melee")
    else:
        player.weapon = Weapon("Bow", 5, 10, "ranged")

def assign_potions(player: Player) -> list[Potion]:
    potions = [
        Potion("Healing Draught", "heal", 10, 1),
        Potion("Healing Draught", "heal", 10, 1),
    ]
    if player.strength >= player.dexterity:
        potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
    else:   
        potions.append(Potion("Cat’s Grace", "buff_dex", 2, 3))
    return potions

def game_turn(player: Player, enemy: Player) -> None:
        potion = player.should_use_potion(enemy)
        if potion is not None:
            result = player.use_potion(potion)
            if "error" not in result:
                if potion.effect == "heal":
                    print(f"\n{player.name} uses {potion.name} (+{result['amount']})")
                else:
                    print(f"\n{player.name} uses {potion.name} ({potion.effect.upper()} +{result['amount']} for {result['duration']} turns)")
            else:
                print(f"\n{player.name} failed to use {potion.name}: {result['error']}")
        damage = player.attack(enemy)
        print(f"{player.name} attack {enemy.name} [{player.weapon.name}, {player.weapon.type}]: inflict {damage} damage")
        print(f"{enemy.name} (HP: {enemy.health}/{enemy.max_health})")

def print_buffs(buffs: list[tuple[str,int,int]]):
    if len(buffs) >= 3:
        return f"{buffs[0]}+{buffs[1]} ({buffs[2]} turns remaining)"
    elif len(buffs) == 2:
        return f"{buffs[0]}+{buffs[1]}"
    elif len(buffs) == 1:
        return buffs[0]
    else:
        return "No active buffs"
    
def main() -> None:
    player1 = Player("Aldren Valemar", 50, 50, randint(1, 20), randint(1, 20), [])
    player1.potions = assign_potions(player1)
    assign_weapon(player1)
    player2 = Player("Lyraen Silvathar", 50, 50, randint(1, 20), randint(1, 20), [])
    player2.potions = assign_potions(player2)
    assign_weapon(player2)
    turn = 0
    while player1.is_alive() and player2.is_alive():
        turn += 1
        print(f"\n=== TURN {turn} ===")
        game_turn(player1, player2)
        if not player2.is_alive():
            break
        game_turn(player2, player1)
        if not player1.is_alive():
            break
        player1.tick_buffs()
        player2.tick_buffs()
        print("\n=== END ROUND: tick buffs ===")
        print(f"\nBuffs attivi:")
        if player1.buffs:
            print(f"{player1.name} {print_buffs(player1.buffs)}")
        if player2.buffs:
            print(f"{player2.name} {print_buffs(player2.buffs)}")
        else:
            print("Nessun buff attivo")
    if player1.is_alive():
        print(f"\n🏆 {player1.name} wins! {player1}")
    else:
        print(f"\n🏆 {player2.name} wins! {player2}")

if __name__ == "__main__":
    main()