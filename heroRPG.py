import random
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
deadpool_quotes = ["It’s so dark. Are you sure you're not from the DC universe?", "Can you speak up? It’s hard to hear you with that pity dick in your mouth.", "Doing the right thing is messy. You want to fight for what's right, sometimes you have to fight dirty.", "It has always been a dream to see my face reflected in your helmet.", "'Let’s Fuck Some Shit Up' is my middle name.", "You don't need to be a superhero to get the girl. The right girl will bring out the hero in you.", "Okay guys, I only have twelve bullets, so you're all going to have to share!", "Oh, hello there! I bet you’re wondering, why the red suit? Well, that’s so bad guys can’t see me bleed!"]

class Character(object):
    def __init__(self, character_type ,health, power):
        self.type = character_type
        self.health = health
        self.power = power

    def attack(self, enemy):
        if enemy.type == "deadpool":
            quote_index = random.randint(0, len(deadpool_quotes))
            print()
            print("Deadpool says: {}".format(deadpool_quotes[quote_index]))
            # print("Deadpool says: {}".format(Deadpool.printQuote(deadpool_quotes, quote_index)))
            print()
            print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            enemy.health -= self.power
            if enemy.health <= 0:
                self.coins += enemy.bounty
                print("{} is dead.".format(enemy.type.capitalize()))
                print("You win {} coins for killing {}".format(enemy.bounty, enemy.type.capitalize()))
        elif enemy.type == "medic":
            if enemy.healing:
                print(enemy.health)
                enemy.health += 2
                print("The {0} healed himself and recuperates 2 health points.".format(enemy.type))
            enemy.health -= self.power
            print()
            print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            if enemy.health <= 0:
                self.coins += enemy.bounty
                print("The {} is dead.".format(enemy.type))
                print("You win {} coins for killing {}".format(enemy.bounty, enemy.type.capitalize()))
        elif enemy.type == "shadow":
            if enemy.takes_hit:
                enemy.health -= self.power
                print()
                print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            else:
                print()
                print("The {0} evades your attack and you do 0 damage to {0}.".format(enemy.type))
            if enemy.health <= 0:
                self.coins += enemy.bounty
                print("The {} is dead.".format(enemy.type))
                print("You win {} coins for killing {}".format(enemy.bounty, enemy.type.capitalize()))
        elif enemy.type != "hero":
            enemy.health -= self.power
            print()
            print("You do {0} damage to the {1}.".format(self.power, enemy.type))
            if enemy.health <= 0:
                self.coins += enemy.bounty
                print("The {} is dead.".format(enemy.type))
                print("You win {} coins for killing {}".format(enemy.bounty, enemy.type.capitalize()))
        else:
            if self.type == "hulk":
                print()
                print("{0} SMASH!!! and does {1} damage to you.".format(self.type.upper(), self.power))
            elif self.type == "deadpool":
                print()
                print("{0} does {1} damage to you.".format(self.type.capitalize(), self.power))
            else:
                print()
                print("The {0} does {1} damage to you.".format(self.type, self.power))
            enemy.health -= self.power
            if enemy.health <= 0:
                print("You are dead.")        
    
    def alive(self):
        if self.health >0:
            return True
        else:
            return False
    
    def print_status(self):
        if self.type == "hero":
            print("You have {} health and {} power. And you have {} coins.".format(self.health, self.power, self.coins))
        else:
            if self.type == "hulk":
                print("{} has {} health and {} power.".format(self.type.upper(), self.health, self.power))
            elif self.type == "deadpool":
                print("{} has {} health and {} power.".format(self.type.capitalize(), self.health, self.power))
            else:
                print("The {} has {} health and {} power.".format(self.type, self.health, self.power))

class Goblin(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.bounty = 25

class Medic(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.bounty = 15

        if random.randint(1,5) == 3:
            self.healing = True
        else:
            self.healing = False

class Zombie(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.damage_reduction = 0
        self.bounty = 100

class Shadow(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.bounty = 50

        if random.randint(1,10) == 5:
            self.takes_hit = True
        else:
            self.takes_hit = False

class Hulk(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.bounty = 250

class Deadpool(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.bounty = 75
    
    def printQuote(deadpool_quotes, quote_index):
            print(len(deadpool_quotes))


class Hero(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.coins = 100
        if random.randint(1,5) == 3:
            self.power = power* 2

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

class Tonic(object):
   cost = 5
   name = 'tonic'
   def apply(self, hero):
       hero.health += 2
    #    print("{}'s health increased to {}.".format(hero.character_type, hero.health))
       print("Hero's health increased to {}.".format(hero.health))

class Sword(object):
   cost = 10
   name = 'sword'
   def apply(self, hero):
       hero.power += 2
    #    print("{}'s power increased to {}.".format(hero.character_type, hero.power))
       print("Hero's power increased to {}.".format(hero.power))


class Store(object):
   # If you define a variable in the scope of a class:
   # This is a class variable and you can access it like
   # Store.items => [Tonic, Sword]

   items = [Tonic, Sword]

   def do_shopping(self, hero):
       while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({} coins)".format(i + 1, item.name, item.cost))
            print("10. leave")

            raw_input = int(input("> "))
            if raw_input == 10:
                break
            else:
                ItemToBuy = Store.items[raw_input - 1]
                item = ItemToBuy()
                hero.buy(item)


def main():
    # character_variable_name = characterClass(character_name, health, power)
    hero = Hero("hero", 10, 5)
    goblin = Goblin("goblin", 6, 2)
    zombie = Zombie("zombie", float("inf"), 3)
    medic = Medic("medic", 9, 3)
    shadow = Shadow("shadow", 20, 1)
    hulk = Hulk("hulk", 50, 10)
    deadpool = Deadpool("deadpool", 15, 4)

    opponent = ""
    random_opponent = random.randint(1,6)
    if random_opponent == 1:
        opponent = goblin
    elif random_opponent == 2:
        opponent = zombie
    elif random_opponent == 3:
        opponent = medic
    elif random_opponent == 4:
        opponent = shadow
    elif random_opponent == 5:
        opponent = hulk
    elif random_opponent == 6:
        opponent = deadpool
    
    else:
        print("FAIL")
    # print(random_opponent)
    # print("You'll be fighting: {}".format(opponent.type))
    
    while opponent.alive() and hero.alive():
        print()
        print()
        hero.print_status()
        opponent.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(opponent.type))
        print("2. do nothing")
        print("3. flee")
        print("4. go to Store")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks opponent
            hero.attack(opponent)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        elif raw_input == "4":
            Store().do_shopping(hero)
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.health > 0:
            # Goblin attacks hero
            opponent.attack(hero)

main()