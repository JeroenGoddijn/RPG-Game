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
        self.healing_bonus = 0
        self.damage_reduction = 0
        self.power_multiplier = 1

    def attack(self, enemy):
        if self.type == "hero":
            self.power_multiplier = 0
            if random.randint(1,5) == 3:
                self.power_multiplier = 2
            else:
                self.power_multiplier = 1
            self.healing_bonus = 0
        # Medic can recuperate 2 health points after being attacked with a probability of 20%
        elif self.type == "medic":
            self.power_multiplier = 1
            self.healing_bonus = 0
            if random.randint(1,5) == 3:
                self.healing_bonus = 2
            else:
                self.healing_bonus = 0
        else:
            self.healing_bonus = 0
            self.power_multiplier = 1

        enemy.health -= self.power * self.power_multiplier
        
        if enemy.type == "zombie":
            print("You do {0} damage to the {1}.".format(self.power * self.power_multiplier, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        elif enemy.type == "shadow":
            if random.randint(1,10) == 5:
                enemy.damage_reduction = self.power
                # print("Shadow damage reduction: {}".format(enemy.damage_reduction))
            else:
                enemy.damage_reduction = 0
                # print("Shadow damage reduction: {}".format(enemy.damage_reduction))
            enemy.health += enemy.damage_reduction
            print("You do {0} damage to the {1}.".format(self.power - self.damage_reduction, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        elif enemy.type == "medic":
            # print(enemy.healing_bonus)
            if enemy.healing_bonus != 0:
                print("The {0} healed himself and recuperates {1} health points.".format(enemy.type, enemy.healing_bonus))
                enemy.health += enemy.healing_bonus
            else:
                enemy.health += enemy.healing_bonus       
            print("You do {0} damage to the {1}.".format(self.power * self.power_multiplier, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        elif enemy.type == "deadpool":
            print("You do {0} damage to {1}.".format(self.power * self.power_multiplier, enemy.type.capitalize()))
            if enemy.health <= 0:
                print("{} is dead.".format(enemy.type.capitalize()))
        elif enemy.type != "hero":
            print("You do {0} damage to the {1}.".format(self.power * self.power_multiplier, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.type))
        else:
            if self.type == "hulk":
                print("{0} SMASH!!! and does {1} damage to you.".format(self.type.upper(), self.power - enemy.damage_reduction))
            elif self.type == "deadpool":
                print("{0} does {1} damage to you.".format(self.type.capitalize(), self.power - enemy.damage_reduction))
            else:
                print("The {0} does {1} damage to you.".format(self.type, self.power - enemy.damage_reduction))
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

def main():
    hero = Character("hero", 10, 5)
    goblin = Character("goblin", 6, 2)
    zombie = Character("zombie", float("inf"), 3)
    medic = Character("medic", 9, 3)
    shadow = Character("shadow", 20, 1)
    hulk = Character("hulk", 50, 10)
    deadpool = Character("deadpool", 15, 4)

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