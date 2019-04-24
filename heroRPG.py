#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero(object):
    def __init__(self, hero_health, hero_power):
        self.health = hero_health
        self.power = hero_power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")
    
    def alive(self):
        if self.health >0:
            return True
        else:
            return False
    
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))


class Goblin(object):
    def __init__(self, goblin_health, goblin_power):
        self.health = goblin_health
        self.power = goblin_power

    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")        

    def alive(self):
        if self.health >0:
            return True
        else:
            return False

    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()