import random
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character(object):
    def __init__(self, character_type ,health, power):
        self.type = character_type
        self.health = health
        self.power = power

    def attack(self, enemy):
        if enemy.type == "deadpool":
            print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            enemy.health -= self.power
            if enemy.health <= 0:
                print("{} is dead.".format(enemy.type.capitalize()))
        elif enemy.type == "medic":
            if enemy.healing:
                print(enemy.health)
                enemy.health += 2
                print("The {0} healed himself and recuperates 2 health points.".format(enemy.type))
            enemy.health -= self.power
            print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        elif enemy.type == "shadow":
            if enemy.takes_hit:
                enemy.health -= self.power
                print("You do {0} damage to {1}.".format(self.power, enemy.type.capitalize()))
            else:
                print("The {0} evades your attack and you do 0 damage to {0}.".format(enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        elif enemy.type != "hero":
            enemy.health -= self.power
            print("You do {0} damage to the {1}.".format(self.power, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        else:
            if self.type == "hulk":
                print("{0} SMASH!!! and does {1} damage to you.".format(self.type.upper(), self.power))
            elif self.type == "deadpool":
                print("{0} does {1} damage to you.".format(self.type.capitalize(), self.power))
            else:
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
            print("You have {} health and {} power.".format(self.health, self.power))
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

class Medic(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        if random.randint(1,5) == 3:
            self.healing = True
        else:
            self.healing = False

class Zombie(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        self.damage_reduction = 0

class Shadow(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)

        if random.randint(1,10) == 5:
            self.takes_hit = True
        else:
            self.takes_hit = False

class Hulk(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)

class Deadpool(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)

class Hero(Character):
    def __init__(self, character_type, health, power):
        Character.__init__(self, character_type, health, power)
        if random.randint(1,5) == 3:
            self.power = power* 2


def main():
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
        hero.print_status()
        opponent.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(opponent.type))
        print("2. do nothing")
        print("3. flee")
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
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.health > 0:
            # Goblin attacks hero
            opponent.attack(hero)

main()