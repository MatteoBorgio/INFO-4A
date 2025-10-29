from player import Player
from weapon import Weapon
from potion import Potion
from random import randint
from random import choice

def assign_name() -> str:
    name_list = [
    "Arvelin", "Kaelor", "Thandric", "Elowen", "Rhaegar",
    "Miralen", "Dareth", "Selindra", "Korvin", "Althira",
    "Aeryn", "Luthien", "Faelar", "Sylwen", "Thalorien",
    "Nimaera", "Elandor", "Seraphiel", "Vaelis", "Caelith",
    "Brokkar", "Thrain", "Durgan", "Hildaen", "Magni",
    "Torvra", "Bofrid", "Kaelda", "Dornik", "Gruntha",
    "Malreth", "Xyra", "Kharzul", "Velthir", "Nergash",
    "Sarynth", "Dravok", "Zephra", "Morwen", "Kalzur",
    "Althorius", "Mirelda", "Seradion", "Ysara", "Velamir",
    "Kaenra", "Thalvion", "Nareth", "Elyndra", "Orveth",
    "Aerion", "Lysara", "Thaless", "Corvian", "Naela",
    "Myrren", "Sireth", "Calandra", "Varyn", "Oryssa"
    ]
    surname_list = [
    "Dawnspear", "Ironforge", "Shadowvale", "Stormborn", "Brightshield",
    "Nightwhisper", "Windrider", "Flameheart", "Moonglade", "Frostbane",
    "Oakenshield", "Dragonsong", "Silverleaf", "Stormbreaker", "Ravencrest",
    "Firebrand", "Emberfall", "Grimstone", "Whisperwind", "Starcrest",
    "Darkbane", "Stronghammer", "Winterfall", "Sunstrider", "Ironheart",
    "Lightbringer", "Mistwalker", "Stonehelm", "Skydancer", "Thornblade",
    "Wildborn", "Brightforge", "Blackthorn", "Ashenvale", "Frostforge",
    "Shadowbane", "Starweaver", "Bloodcrest", "Windwatcher", "Goldmantle",
    "Ironbeard", "Moonbrook", "Silverflame", "Stormwatch", "Fireweaver",
    "Runeborn", "Shadowbrook", "Thornbreaker", "Wolfsong", "Skywarden"
    ]   
    name = choice(name_list)
    surname = choice(surname_list)
    return name + " " + surname

def assign_weapon(player: Player) -> None:
    melee_weapons = [
    Weapon("Longsword", 5, 9, "melee"),
    Weapon("Battle Axe", 6, 10, "melee"),
    Weapon("Mace", 4, 8, "melee"),
    Weapon("Dagger", 2, 5, "melee"),
    Weapon("Warhammer", 7, 11, "melee"),
    Weapon("Greatsword", 8, 12, "melee"),
    Weapon("Sabre", 4, 7, "melee"),
    Weapon("Spear", 5, 8, "melee"),
    Weapon("War Scythe", 6, 9, "melee"),
    Weapon("Halberd", 7, 10, "melee")
    ]
    ranged_weapons = [
    Weapon("Longbow", 5, 9, "ranged"),
    Weapon("Shortbow", 3, 7, "ranged"),
    Weapon("Light Crossbow", 4, 8, "ranged"),
    Weapon("Heavy Crossbow", 6, 10, "ranged"),
    Weapon("Reinforced Sling", 2, 5, "ranged"),
    Weapon("Throwing Spear", 5, 9, "ranged"),
    Weapon("Chakram", 4, 8, "ranged"),
    Weapon("Elven Bow", 6, 10, "ranged"),
    Weapon("Gem-Tipped Darts", 3, 6, "ranged"),
    Weapon("Runic Staff", 4, 9, "ranged")
    ]
    if player.strength > player.dexterity:
        player.weapon = choice(melee_weapons)
    else:
        player.weapon = choice(ranged_weapons)

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
    player1 = Player(assign_name(), 50, 50, randint(1, 20), randint(1, 20), [])
    player1.potions = assign_potions(player1)
    assign_weapon(player1)
    player2 = Player(assign_name(), 50, 50, randint(1, 20), randint(1, 20), [])
    player2.potions = assign_potions(player2)
    assign_weapon(player2)
    turn = 0
    print("\n=== CODE COMBAT SIMULATION ===\n")
    print(f"{player1.name} ({player1.health}/{player1.max_health}): Strength = {player1.strength}, Dexterity = {player1.dexterity}")
    print(f"{player2.name} ({player2.health}/{player2.max_health}): Strength = {player2.strength}, Dexterity = {player2.dexterity}\n")
    print(f"{player1.name} equip {player1.weapon.name} ({player1.weapon.min_damage}/{player1.weapon.max_damage})")
    print(f"{player2.name} equip {player2.weapon.name} ({player2.weapon.min_damage}/{player2.weapon.max_damage})")
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