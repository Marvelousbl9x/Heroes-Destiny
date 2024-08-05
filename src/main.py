print("Hello heroes")
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
            damage += 20  # Extra damage from the sword
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
            self.temp_damage_bonus = 25
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

# Game logic
def create_monster():
    monsters = [
        Monster("Alien", 30, 10),
        Monster("Croco", 50, 15),
        Monster("Mantis", 70, 20),
        Monster("Mutant", 50, 15),
        Monster("skodbodoo", 40, 20),
        Monster("Clock",  50, 30),
        Monster("Witch", 60, 10),
        Monster("Bugaboo", 75, 35),
    ]
    return random.choice(monsters)

def create_boss():
    bosses = [
        Boss("GLaDOS", 400, 25),
        Boss("G-Man", 450, 30),
        Boss("Ohio skibidi sigma", 500, 30),
    ]
    return random.choice(bosses)

def encounter(player):
    print("\nYou enter a new room...")
    if random.choice([True, False]):
        monster = create_monster()
        print(f"You encounter a monster named {monster.name}!")
        while monster.is_alive() and player.is_alive():
            action = input("Do you want to (a)ttack, (r)un, use (p)otion, use (g)ift card, or eat (c)hicken nuggets? ").strip().lower()
            if action == 'a':
                damage = player.attack()
                monster.take_damage(damage)
                print(f"You deal {damage} damage to the {monster.name}.")
                if monster.is_alive():
                    player.take_damage(monster.damage)
                    print(f"The {monster.name} deals {monster.damage} damage to you.")
            elif action == 'r':
                if random.choice([True, False]):
                    print("You successfully ran away!")
                    break
                else:
                    player.take_damage(monster.damage)
                    print(f"The {monster.name} hits you as you flee, dealing {monster.damage} damage.")
                    break
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
    else:
        item = random.choice(["health potion", "gold coin", "sword", "robux gift card", "chicken nuggets"])
        player.inventory[item] += 1
        print(f"You found a {item}!")

def shop(player):
    print("\nWelcome to the 24/7 shop!")
    print(f"Your inventory: {player.inventory}")
    print("1. Buy health potion (2 gold coins)")
    print("2. Buy sword (3 gold coins)")
    print("3. Buy Robux gift card (5 gold coins)")
    print("4. Buy chicken nuggets (4 gold coins)")
    print("5. Exit shop")

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
            print("Exiting shop.")
            break
        else:
            print("Invalid choice. Please try again.")

def trader(player):
    print("\nYou have encountered a trader! You can sell your items at a high price.")
    item_prices = {
        "sword": 10,
        "health potion": 5,
        "robux gift card": 20,
        "chicken nuggets": 8,
    }
    print(f"Your inventory: {player.inventory}")
    for item, price in item_prices.items():
        if player.inventory[item] > 0:
            sell = input(f"Do you want to sell your {item}(s) for {price} gold coins each? (y/n): ").strip().lower()
            if sell == 'y':
                player.inventory["gold coin"] += player.inventory[item] * price
                player.inventory[item] = 0
                print(f"You sold your {item}(s)!")
    print(f"Your updated inventory: {player.inventory}")

def math_minigame():
    print("\nYou have entered a room filled with landmines!")
    questions = [
        {"question": "What is the derivative of x^2?", "answer": "2x"},
        {"question": "Solve for x: 2x + 3 = 7", "answer": "2"},
        {"question": "What is the integral of 1/x?", "answer": "ln|x|"},
        {"question": "What is 12 * 14?", "answer": "168"},
        {"question": "What is the square root of 144?", "answer": "12"}
    ]
    question = random.choice(questions)
    print(f"Answer the question correctly to proceed: {question['question']}")
    answer = input("Your answer: ").strip()
    if answer == question["answer"]:
        print("You answered correctly and avoided the landmines!")
    else:
        print("You answered incorrectly and triggered a landmine. You have died.")
        return False
    return True

def pursuit(player):
    print("\nThe pursuit of a boss has begun! You will face challenges and hear voice lines as you chase the boss.")
    voice_lines = [
        "You'll never catch me!",
        "I am the ultimate power!",
        "You are too weak to defeat me!",
        "I will crush you!",
        "Run all you want, it won't save you!"
    ]
    challenges = [
        "Solve this riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (answer: echo)",
        "Solve this math problem: What is 25 + 37? (answer: 62)",
        "Guess the number I'm thinking of between 1 and 10. (answer: 7)"
    ]

    for i in range(5):
        print(random.choice(voice_lines))
        challenge = random.choice(challenges)
        print(challenge.split(": ")[1])
        answer = input("Your answer: ").strip().lower()
        if answer != challenge.split(": ")[2].strip("()").split(": ")[1]:
            print("You failed the challenge and the pursuit has ended.")
            player.take_damage(50)
            break
        else:
            print("You passed the challenge and continue the pursuit.")
        
def boss_fight(player):
    boss = create_boss()
    print(f"\nA powerful boss named {boss.name} appears!")
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

def game():
    print("Welcome to Hero's Destiny!")
    name = input("Enter your character's name: ").strip()
    player = Player(name)
    turns_survived = 0
    boss_turn = 100
    
    while player.is_alive():
        if turns_survived == 25:
            if not math_minigame():
                break
        
        if turns_survived == 50:
            trader(player)

        if turns_survived == 75:
            pursuit(player)
        
        encounter(player)
        player.temp_damage_bonus = 0  # Reset temporary damage bonus after each encounter
        turns_survived += 1

        if turns_survived == boss_turn:
            boss_fight(player)
            if player.is_alive():
                print(f"\nCongratulations! You defeated the boss and won the game. Hope you didn't run like a coward and just went straight for the boss!")
            break

        if not player.is_alive():
            print("\nYou have died. Your destiny came to an end!")
            break
        
        if turns_survived in [6, 9, 15, 28, 35, 51, 65, 74]:
            shop(player)

        continue_game = input("Do you want to continue exploring? (y/n) ").strip().lower()
        if continue_game == 'n':
            print("Exiting the game. Thanks for playing!")
            break
        elif continue_game != 'y':
            print("Invalid choice. The game will now end.")
            break
         
    
    if player.is_alive() and turns_survived != boss_turn:
        print("\nGame Over. Thanks for playing!")
        print(f"{player.name}'s final stats: HP = {player.hp}, Inventory = {player.inventory}")

# Start the game
if __name__ == "__main__":
    game()
    








        