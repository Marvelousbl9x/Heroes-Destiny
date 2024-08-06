import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = {
            "sword": 0,
            "gold coin": 10,  # Start with some gold coins for purchasing
            "health potion": 0,
            "robux gift card": 0,
            "chicken nuggets": 0
        }
        self.base_damage = 10
        self.temp_damage_bonus = 0
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
    
    def attack(self):
        damage = self.base_damage + self.temp_damage_bonus
        if self.inventory["sword"] > 0:
            damage += 10  # Extra damage from the sword
        return damage
    
    def use_robux_gift_card(self):
        if self.inventory["robux gift card"] > 0:
            self.hp = 100
            self.inventory["robux gift card"] -= 1
            print("You used a Robux gift card and restored your health to full!")
        else:
            print("You don't have any Robux gift cards!")
    
    def use_chicken_nuggets(self):
        if self.inventory["chicken nuggets"] > 0:
            self.temp_damage_bonus = 5
            self.inventory["chicken nuggets"] -= 1
            print("You ate chicken nuggets and gained a temporary damage boost!")
        else:
            print("You don't have any chicken nuggets!")

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0

class Boss(Monster):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

# Define monsters
def create_monster():
    monsters = [
        Monster("Goblin", 30, 10),
        Monster("Orc", 50, 15),
        Monster("Troll", 70, 20),
        Monster("Skeleton", 40, 12),
        Monster("Zombie", 60, 18),
        Monster("Vampire", 80, 22),
        Monster("Werewolf", 90, 25),
        Monster("Dragon", 100, 30),
        Monster("Golem", 120, 35),
        Monster("Giant Spider", 110, 28)
    ]
    return random.choice(monsters)

def create_boss():
    return Boss("Ohio Skibidi Sigma", 500, 30)

def land_mine_room(player):
    print("\nYou entered a room with land mines!")
    print("Solve these math problems to escape:")
    problems = [
        ("12 * 7", 84),
        ("60 + 9", 69),
        ("13 - 4", 9),
        ("50 / 10", 5)
    ]
    for problem, answer in problems:
        user_answer = int(input(f"What is {problem}? "))
        if user_answer != answer:
            print("Incorrect answer. You stepped on a land mine and died instantly. Game Over.")
            return False
    print("You successfully solved the problems and escaped the room.")
    return True

def trader(player):
    print("\nYou encounter a trader!")
    print(f"Your inventory: {player.inventory}")
    print("1. Buy health potion (2 gold coins)")
    print("2. Buy sword (3 gold coins)")
    print("3. Buy Robux gift card (5 gold coins)")
    print("4. Buy chicken nuggets (4 gold coins)")
    print("5. Exit trader")

    while True:
        choice = input("What would you like to do? (1/2/3/4/5): ").strip()
        if choice == '1':
            if player.inventory["gold coin"] >= 2:
                player.inventory["gold coin"] -= 2
                player.inventory["health potion"] += 1
                print("You bought a health potion!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '2':
            if player.inventory["gold coin"] >= 3:
                player.inventory["gold coin"] -= 3
                player.inventory["sword"] += 1
                print("You bought a sword!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '3':
            if player.inventory["gold coin"] >= 5:
                player.inventory["gold coin"] -= 5
                player.inventory["robux gift card"] += 1
                print("You bought a Robux gift card!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '4':
            if player.inventory["gold coin"] >= 4:
                player.inventory["gold coin"] -= 4
                player.inventory["chicken nuggets"] += 1
                print("You bought chicken nuggets!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '5':
            print("Exiting trader.")
            break
        else:
            print("Invalid choice. Please try again.")

def trader_turn_50(player):
    print("\nYou encounter a trader!")
    print(f"Your inventory: {player.inventory}")
    print("1. Buy health potion (2 gold coins)")
    print("2. Buy sword (3 gold coins)")
    print("3. Buy Robux gift card (5 gold coins)")
    print("4. Buy chicken nuggets (4 gold coins)")
    print("5. Sell items")
    print("6. Exit trader")

    while True:
        choice = input("What would you like to do? (1/2/3/4/5/6): ").strip()
        if choice == '1':
            if player.inventory["gold coin"] >= 2:
                player.inventory["gold coin"] -= 2
                player.inventory["health potion"] += 1
                print("You bought a health potion!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '2':
            if player.inventory["gold coin"] >= 3:
                player.inventory["gold coin"] -= 3
                player.inventory["sword"] += 1
                print("You bought a sword!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '3':
            if player.inventory["gold coin"] >= 5:
                player.inventory["gold coin"] -= 5
                player.inventory["robux gift card"] += 1
                print("You bought a Robux gift card!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '4':
            if player.inventory["gold coin"] >= 4:
                player.inventory["gold coin"] -= 4
                player.inventory["chicken nuggets"] += 1
                print("You bought chicken nuggets!")
            else:
                print("You don't have enough gold coins!")
        elif choice == '5':
            print("You can sell your items:")
            for item, count in player.inventory.items():
                if item != "gold coin" and count > 0:
                    sell_choice = input(f"Do you want to sell {count} {item}(s)? (y/n): ").strip().lower()
                    if sell_choice == 'y':
                        player.inventory["gold coin"] += count
                        player.inventory[item] = 0
                        print(f"You sold {count} {item}(s) for {count} gold coin(s).")
            print(f"Your inventory: {player.inventory}")
        elif choice == '6':
            print("Exiting trader.")
            break
        else:
            print("Invalid choice. Please try again.")

def ask_boss_questions(player):
    questions = [
        ("What has keys but can't open locks?", "piano"),
        ("What has a head and a tail but no body?", "coin"),
        ("What gets wetter as it dries?", "towel"),
        ("What has to be broken before you can use it?", "egg"),
        ("What can travel around the world while staying in a corner?", "stamp"),
        ("What is full of holes but still holds water?", "sponge"),
        ("What has an eye but can't see?", "needle"),
        ("What has a heart that doesn't beat?", "artichoke"),
        ("What comes down but never goes up?", "rain"),
        ("What begins with T, ends with T, and has T in it?", "teapot"),
        ("What is so fragile that saying its name breaks it?", "silence"),
        ("What is always in front of you but can't be seen?", "future"),
        ("What has four fingers and a thumb but isn't alive?", "glove"),
        ("What is easy to get into but hard to get out of?", "trouble"),
        ("What has cities but no houses, forests but no trees, and rivers but no water?", "map")
    ]
    
    for question, answer in questions:
        user_answer = input(question + " ").strip().lower()
        if user_answer != answer:
            player.take_damage(50)
            print("Incorrect answer. You lost 50 HP.")
        else:
            print("Correct answer!")
    
    if player.is_alive():
        print("You successfully answered all questions and dealt 100 damage to the boss.")
        return True
    else:
        print("You didn't survive the questions. Game Over.")
        return False

def boss_preview(player):
    print("\nYou see a preview of the boss: Ohio Skibidi Sigma.")
    choice = input("Do you want to pursue the boss? (y/n): ").strip().lower()
    if choice == 'y':
        return True
    return False

def boss_fight(player):
    boss = create_boss()
    print(f"\nThe boss {boss.name} appears with {boss.hp} HP!")
    
    while boss.is_alive() and player.is_alive():
        action = input("Do you want to (a)ttack, use (g)ift card, or eat (c)hicken nuggets? ").strip().lower()
        if action == 'a':
            damage = player.attack()
            boss.take_damage(damage)
            print(f"You deal {damage} damage to the {boss.name}.")
            if boss.is_alive():
                player.take_damage(boss.damage)
                print(f"The {boss.name} deals {boss.damage} damage to you.")
        elif action == 'g':
            player.use_robux_gift_card()
        elif action == 'c':
            player.use_chicken_nuggets()
        else:
            print("Invalid action.")
    
    if player.is_alive():
        print("Congratulations! You defeated the boss and won the game!")
    else:
        print("You were defeated by the boss. Game Over.")

def encounter(player, turn):
    if turn % 3 == 0:  # Every third turn, find items
        items = ["sword", "health potion", "robux gift card", "chicken nuggets"]
        item = random.choice(items)
        player.inventory[item] += 1
        print(f"You found a {item}!")
    else:  # Otherwise, encounter a monster
        monster = create_monster()
        print(f"A wild {monster.name} appears!")
        while monster.is_alive() and player.is_alive():
            action = input("Do you want to (a)ttack, (r)un, use (g)ift card, or eat (c)hicken nuggets? ").strip().lower()
            if action == 'a':
                damage = player.attack()
                monster.take_damage(damage)
                print(f"You deal {damage} damage to the {monster.name}.")
                if monster.is_alive():
                    player.take_damage(monster.damage)
                    print(f"The {monster.name} deals {monster.damage} damage to you.")
            elif action == 'r':
                if random.random() < 0.8:  # 80% chance to escape
                    print("You successfully ran away!")
                    break
                else:
                    damage = random.randint(5, 15)
                    player.take_damage(damage)
                    print(f"While running away, you got hurt and lost {damage} HP.")
            elif action == 'g':
                player.use_robux_gift_card()
            elif action == 'c':
                player.use_chicken_nuggets()
            else:
                print("Invalid action.")
    
    if not player.is_alive():
        print("You have been defeated. Game Over.")
        return False
    return True

def game():
    name = input("Enter your character name: ")
    player = Player(name)
    pursue_boss = False
    
    for turn in range(1, 101):
        if turn == 25:
            if not land_mine_room(player):
                break
        elif turn in [7, 11, 15, 21, 29, 38, 43, 51, 68, 73]:
            trader(player)
        elif turn == 50:
            trader_turn_50(player)
        elif turn == 75:
            pursue_boss = boss_preview(player)
        elif 75 < turn <= 90 and pursue_boss:
            if not ask_boss_questions(player):
                break
        elif turn == 100:
            boss_fight(player)
            break
        else:
            if not encounter(player, turn):
                break
    
    print("\nGame Over!")
    print(f"Player: {player.name}")
    print(f"HP: {player.hp}")
    print(f"Inventory: {player.inventory}")
    print("Thanks for playing!")

# Start the game
game()
