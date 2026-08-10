import json
import os
import random

CLASSES = {
    "1": {"name": "Warrior", "hp": 150, "mana": 40, "atk": 18, "def": 12, "skill": "Slash", "s_cost": 10, "s_dmg": 25},
    "2": {"name": "Mage",    "hp": 90,  "mana": 120,"atk": 22, "def": 4,  "skill": "Fireball", "s_cost": 15, "s_dmg": 35},
    "3": {"name": "Archer",  "hp": 110, "mana": 70, "atk": 16, "def": 8,  "skill": "Sniper Shot", "s_cost": 15, "s_dmg": 30},
    "4": {"name": "Assassin","hp": 80,  "mana": 60, "atk": 25, "def": 3,  "skill": "Backstab", "s_cost": 15, "s_dmg": 40},
}

WEAPONS = [
    {"name": "Wooden Sword", "bonus_atk": 0,  "price": 0},
    {"name": "Iron Sword",   "bonus_atk": 10, "price": 100},
    {"name": "Flame Sword",  "bonus_atk": 25, "price": 500},
    {"name": "Dragon Blade", "bonus_atk": 50, "price": 2000},
]

ARMOR = [
    {"name": "Cloth Tunic", "bonus_def": 0,  "price": 0},
    {"name": "Iron Plate",  "bonus_def": 10, "price": 100},
    {"name": "Titan Armor", "bonus_def": 25, "price": 500},
]

BOSSES = [
    "Goblin King", "Forest Guardian", "Ancient Golem", "Vampire Lord", "Dragon Rider",
    "Demon General", "Ice Titan", "Shadow Emperor", "Celestial Dragon", "Ancient Demon King"
]

player = {
    "name": "Hero",
    "class": "Warrior",
    "level": 1,
    "exp": 0,
    "exp_needed": 100,
    "hp": 150,
    "max_hp": 150,
    "mana": 40,
    "max_mana": 40,
    "atk": 18,
    "def": 12,
    "skill_name": "Slash",
    "skill_cost": 10,
    "skill_dmg": 25,
    "gold": 50,
    "potions": 3,
    "weapon_idx": 0,
    "armor_idx": 0,
    "bosses_defeated": 0,
}


def get_total_atk():
    return player["atk"] + WEAPONS[player["weapon_idx"]]["bonus_atk"]

def get_total_def():
    return player["def"] + ARMOR[player["armor_idx"]]["bonus_def"]

def check_level_up():
    while player["exp"] >= player["exp_needed"]:
        if player["level"] % 10 == 0 and player["bosses_defeated"] < (player["level"] // 10):
            print("\n[!] Level Cap Reached! Defeat the Region Boss to continue leveling up.")
            player["exp"] = player["exp_needed"] - 1
            break

        player["exp"] -= player["exp_needed"]
        player["level"] += 1
        player["exp_needed"] += 50

        player["max_hp"] += 15
        player["max_mana"] += 10
        player["atk"] += 3
        player["def"] += 2
        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]

        print(f"\n🎉 LEVEL UP! You reached Level {player['level']}!")

def save_game():
    with open("savegame.json", "w") as f:
        json.dump(player, f)
    print("\n[+] Game Saved Successfully!")

def load_game():
    global player
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            player = json.load(f)
        print("\n[+] Game Loaded Successfully!")
        return True
    print("\n[-] Save file not found.")
    return False


def battle(is_boss=False):
    if is_boss:
        b_idx = player["bosses_defeated"]
        if b_idx >= 10:
            print("\nAll bosses have been defeated!")
            return
        e_name = f"BOSS: {BOSSES[b_idx]}"
        e_hp = 100 + (b_idx + 1) * 80
        e_atk = 15 + (b_idx + 1) * 5
        e_exp = 200 + b_idx * 100
        e_gold = 100 + b_idx * 50
    else:
        e_name = f"Wild Monster (Lvl {player['level']})"
        e_hp = 30 + player["level"] * 15
        e_atk = 8 + player["level"] * 2
        e_exp = 30 + player["level"] * 10
        e_gold = 15 + player["level"] * 5

    e_max_hp = e_hp
    defending = False

    print(f"\n--- BATTLE START: {player['name']} VS {e_name} ---")

    while player["hp"] > 0 and e_hp > 0:
        print(f"\n{player['name']} | HP: {player['hp']}/{player['max_hp']} | Mana: {player['mana']}/{player['max_mana']}")
        print(f"{e_name} | HP: {e_hp}/{e_max_hp}")
        print("1. Attack  2. Skill  3. Heal Potion  4. Defend  5. Run")

        choice = input("> Choose action: ").strip()

        if choice == "1":
            dmg = max(1, get_total_atk() - 2)
            print(f"You attacked {e_name} for {dmg} damage!")
            e_hp -= dmg

        elif choice == "2":
            if player["mana"] < player["skill_cost"]:
                print("[-] Not enough Mana!")
                continue
            player["mana"] -= player["skill_cost"]
            dmg = player["skill_dmg"] + get_total_atk()
            print(f"✨ Used {player['skill_name']} for {dmg} damage!")
            e_hp -= dmg

        elif choice == "3":
            if player["potions"] <= 0:
                print("[-] No potions remaining!")
                continue
            player["potions"] -= 1
            player["hp"] = min(player["max_hp"], player["hp"] + 50)
            print(f"[+] Used a Potion! Restored 50 HP. ({player['potions']} remaining)")

        elif choice == "4":
            defending = True
            print("🛡️ You prepare to brace for the incoming attack!")

        elif choice == "5":
            if is_boss:
                print("[-] You cannot flee from a boss fight!")
                continue
            print("🏃 Escaped successfully!")
            return

        if e_hp <= 0:
            print(f"\n🎉 Defeated {e_name}!")
            player["gold"] += e_gold
            player["exp"] += e_exp
            print(f"[+] Obtained {e_gold} Gold and {e_exp} EXP.")

            if is_boss:
                player["bosses_defeated"] += 1
                print("🏆 Boss defeated! Next region unlocked.")

            check_level_up()
            return

        e_dmg = max(1, e_atk - get_total_def())
        if defending:
            e_dmg = e_dmg // 2
            defending = False

        player["hp"] -= e_dmg
        print(f"{e_name} hit you for {e_dmg} damage!")

        if player["hp"] <= 0:
            print("\n💀 You were defeated in battle...")
            return

def shop():
    while True:
        print(f"\n--- VILLAGE SHOP (Gold: {player['gold']}) ---")
        print("1. Buy Weapons")
        print("2. Buy Armor")
        print("3. Buy Potions (15 Gold)")
        print("4. Exit Shop")

        choice = input("> Choose: ").strip()

        if choice == "1":
            print("\nWEAPONS:")
            for i, w in enumerate(WEAPONS):
                print(f"{i+1}. {w['name']} (+{w['bonus_atk']} Atk) - {w['price']} Gold")
            c = input("> Select weapon number (0 to cancel): ").strip()
            if c.isdigit() and 0 < int(c) <= len(WEAPONS):
                idx = int(c) - 1
                if player["gold"] >= WEAPONS[idx]["price"]:
                    player["gold"] -= WEAPONS[idx]["price"]
                    player["weapon_idx"] = idx
                    print(f"[+] Equipped {WEAPONS[idx]['name']}!")
                else:
                    print("[-] Not enough gold!")

        elif choice == "2":
            print("\nARMOR:")
            for i, a in enumerate(ARMOR):
                print(f"{i+1}. {a['name']} (+{a['bonus_def']} Def) - {a['price']} Gold")
            c = input("> Select armor number (0 to cancel): ").strip()
            if c.isdigit() and 0 < int(c) <= len(ARMOR):
                idx = int(c) - 1
                if player["gold"] >= ARMOR[idx]["price"]:
                    player["gold"] -= ARMOR[idx]["price"]
                    player["armor_idx"] = idx
                    print(f"[+] Equipped {ARMOR[idx]['name']}!")
                else:
                    print("[-] Not enough gold!")

        elif choice == "3":
            if player["gold"] >= 15:
                player["gold"] -= 15
                player["potions"] += 1
                print("[+] Bought 1 Health Potion!")
            else:
                print("[-] Not enough gold!")

        elif choice == "4":
            break

def main():
    print("==========================================")
    print("      LEGENDS OF THE FORGOTTEN REALM      ")
    print("==========================================")
    print("1. New Game\n2. Load Game\n3. Exit")
    c = input("> Choose option: ").strip()

    if c == "1":
        player["name"] = input("Enter Hero Name: ").strip() or "Hero"
        print("\nSelect Class:")
        for k, v in CLASSES.items():
            print(f"{k}. {v['name']} (HP: {v['hp']}, Mana: {v['mana']}, Atk: {v['atk']}, Def: {v['def']})")
        
        cls_choice = input("> Select Class (1-4): ").strip()
        if cls_choice not in CLASSES:
            cls_choice = "1"

        cdata = CLASSES[cls_choice]
        player["class"] = cdata["name"]
        player["hp"] = player["max_hp"] = cdata["hp"]
        player["mana"] = player["max_mana"] = cdata["mana"]
        player["atk"] = cdata["atk"]
        player["def"] = cdata["def"]
        player["skill_name"] = cdata["skill"]
        player["skill_cost"] = cdata["s_cost"]
        player["skill_dmg"] = cdata["s_dmg"]

    elif c == "2":
        if not load_game():
            return
    else:
        return

    while player["hp"] > 0:
        if player["bosses_defeated"] >= 10:
            print(f"\n🏆 CONGRATULATIONS {player['name']}! YOU DEFEATED THE ANCIENT DEMON KING AND SAVED ELDORIA!")
            break

        print("\n==========================================")
        print(f"Hero: {player['name']} (Lvl {player['level']} {player['class']}) | HP: {player['hp']}/{player['max_hp']}")
        print(f"Gold: {player['gold']} | Weapon: {WEAPONS[player['weapon_idx']]['name']} | Armor: {ARMOR[player['armor_idx']]['name']}")
        print("==========================================")
        print("1. Explore (Battle)")
        print(f"2. Challenge Boss ({BOSSES[player['bosses_defeated']]})")
        print("3. Shop")
        print("4. Save Game")
        print("5. Save & Exit")

        choice = input("> Choose action: ").strip()

        if choice == "1":
            battle(is_boss=False)
        elif choice == "2":
            battle(is_boss=True)
        elif choice == "3":
            shop()
        elif choice == "4":
            save_game()
        elif choice == "5":
            save_game()
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()