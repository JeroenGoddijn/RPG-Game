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
        enemy.health -= self.power
        if enemy.type != "hero":
            print("You do {0} damage to the {1}.".format(self.power, enemy.type))
            if enemy.health <= 0:
                print("The {} is dead.", enemy.type)
        else:
            print("The {0} does {1} damage to you.".format(self.type, self.power))
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
            print("The {} has {} health and {} power.".format(self.type, self.health, self.power))

def main():
    hero = Character("hero", 10, 5)
    goblin = Character("goblin", 6, 2)
    zombie = Character("zombie", float("inf"), 3)

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        # print("1. fight goblin")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.health > 0:
            # Goblin attacks hero
            zombie.attack(hero)

main()