import random

# Game entities
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = {
            "sword": 0,
            "gold coin": 0,
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
    return Boss("G-Man", 500, 30)

def land_mine_room(player):
    print("\nYou entered a room with land mines!")
    print("Solve these math problems to escape:")
    problems = [
        (12 * 7, 84),
        (56 / 8, 7),
        (18 + 29, 47),
        (144 - 88, 56),
        (23 * 15, 345)
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

def ask_boss_questions(player):
    questions = [
        ("What is 5 + 7?", 12),
        ("What is 9 * 6?", 54),
        ("What is 144 / 12?", 12),
        ("What is 20 - 8?", 12),
        ("What is 15 * 4?", 60),
        ("What is 81 / 9?", 9),
        ("What is 25 + 30?", 55),
        ("What is 100 - 45?", 55),
        ("What is 8 * 7?", 56),
        ("What is 14 + 9?", 23)
    ]
    
    for question, answer in random.sample(questions, 5):
        user_answer = int(input(question + " "))
        if user_answer != answer:
            player.take_damage(50)
            print("Incorrect answer. You lose 50 HP.")
            if not player.is_alive():
                print("You have been defeated. Game Over.")
                return False
    return True

def boss_fight(player):
    boss = create_boss()
    print(f"\nA powerful {boss.name} appears!")
    
    # Boss questions between turns 75 and 90
    if 75 <= turn <= 90:
        print("The boss is asking questions to weaken you before the final fight!")
        if not ask_boss_questions(player):
            return False
    
    while boss.is_alive() and player.is_alive():
        action = input("Do you want to (a)ttack, use (p)otion, use (g)ift card, or eat (c)hicken nuggets? ").strip().lower()
        if action == 'a':
            damage = player.attack()
            boss.take_damage(damage)
            print(f"You deal {damage} damage to {boss.name}.")
            if boss.is_alive():
                player.take_damage(boss.damage)
                print(f"{boss.name} deals {boss.damage} damage to you.")
        elif action == 'p':
            if player.inventory["health potion"] > 0:
                player.heal(20)
                player.inventory["health potion"] -= 1
                print("You use a health potion and heal 20 HP.")
            else:
                print("You don't have any health potions!")
        elif action == 'g':
            player.use_robux_gift_card()
        elif action == 'c':
            player.use_chicken_nuggets()
        else:
            print("Invalid action.")
    
    if not player.is_alive():
        print(f"\nYou were defeated by {boss.name}. Game Over.")
    else:
        print(f"\nCongratulations! You defeated the boss and won the game!")

def boss_preview(player):
    print("\nYou see a preview of the boss!")
    print("The boss is strong, but you have the option to pursue it now.")
    action = input("Do you want to pursue the boss? (y/n) ").strip().lower()
    if action == 'y':
        # Pursue the boss
        if random.choice([True, False]):
            print("You successfully pursued the boss and dealt 100 damage!")
            return True
        else:
            print("You failed the pursuit and suffered 50 damage.")
            player.take_damage(50)
            return False
    return True

def encounter(player, turn):
    print("\nYou enter a new room...")
    
    # Randomly decide if an item is found
    if random.random() < 0.2:  # 20% chance to find an item
        items = [
            ("sword", "You found a sword on the ground!"),
            ("health potion", "You found a health potion on the ground!"),
            ("robux gift card", "You found a Robux gift card on the ground!"),
            ("chicken nuggets", "You found chicken nuggets on the ground!")
        ]
        item, message = random.choice(items)
        print(message)
        player.inventory[item] += 1

    if turn in [7, 11, 19, 27, 38, 45, 63, 71]:
        shop(player)
    elif turn == 25:
        if not land_mine_room(player):
            return False
    elif turn == 50:
        trader(player)
    elif turn == 75:
        if not boss_preview(player):
            return False
    return True

def main():
    global turn
    name = input("Enter your character's name: ").strip()
    player = Player(name)
    
    turn = 0
    while player.is_alive() and turn < 100:
        turn += 1
        print(f"\nTurn {turn}")
        if not encounter(player, turn):
            break
        if turn == 100:
            boss_fight(player)
    
    if player.is_alive() and turn == 100:
        print("Congratulations, you survived the dungeon and defeated the final boss!")

if __name__ == "__main__":
    main()
    