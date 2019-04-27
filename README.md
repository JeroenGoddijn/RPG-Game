RPG Game 1

Take the RPG game and rewrite it using objects.

Fork Hero RPG Starting Template

As you complete each step, commit, push, and tag the final working version. In the future we'll base a refactor off of one the steps.

Step 1

Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health and goblin_powerall through out the app.

Step 2

Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)

Step 3

Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero).

Step 4

Refactor the while condition:

while goblin.health > 0 and hero.health > 0:
to

while goblin.alive() and hero.alive():
The health checks should be moved to within the alive methods of Hero and Goblin respectively.

Step 5

Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the same for the goblin.

Step 6

Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called Characterand make both Hero and Goblin inherit from it.

Step 7

The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and Goblin - now they can simply inherit it from Character.

Step 7: Bonus Challenge

The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to move them into the Character class as well? Give it a try.

Step 8: Bonus Challenge 2

Create a zombie character that cannot die and have it fight the hero instead of the goblin.


############################################################################################################

Hero RPG Game: Part 2

You will base your game on version 7 of the game and make mods to the game.

Characters

make the hero generate double damage points during an attack with a probability of 20%
make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
make a Zombie character that doesn't die even if his health is below zero
come up with at least two other characters with their individual characteristics, and implement them.
Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.
Items

make a SuperTonic item to the store, it will restore the hero back to 10 health points.
add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.
Bonus

allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
there is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.
Version 5 Reference implementation

 

 

#!/usr/bin/env python3

 

"""

Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.

"""

 

import random

import time

 

class Character(object):

   def __init__(self):

       self.name = '<undefined>'

       self.health = 10

       self.power = 5

       self.coins = 20

 

   def alive(self):

       return self.health > 0

 

   def attack(self, enemy):

       if not self.alive():

           return

       print("{} attacks {}".format(self.name, enemy.name))

       enemy.receive_damage(self.power)

       time.sleep(1.5)

 

   def receive_damage(self, points):

       self.health -= points

       print("{} received {} damage.".format(self.name, points))

       if self.health <= 0:

           print("{} is dead.".format(self.name))

 

   def print_status(self):

       print("{} has {} health and {} power.".format(self.name, self.health, self.power))

 

class Hero(Character):

   def __init__(self):

       self.name = 'hero'

       self.health = 10

       self.power = 5

       self.coins = 20

 

   def restore(self):

       self.health = 10

       print("Hero's heath is restored to {}!".format(self.health))

       time.sleep(1)

 

   def buy(self, item):

       self.coins -= item.cost

       item.apply(hero)

 

class Goblin(Character):

   def __init__(self):

       self.name = 'goblin'

       self.health = 6

       self.power = 2

 

class Wizard(Character):

   def __init__(self):

       self.name = 'wizard'

       self.health = 8

       self.power = 1

 

   def attack(self, enemy):

       swap_power = random.random() > 0.5

       if swap_power:

           print("{} swaps power with {} during attack".format(self.name, enemy.name))

           self.power, enemy.power = enemy.power, self.power

       super(Wizard, self).attack(enemy)

       if swap_power:

           self.power, enemy.power = enemy.power, self.power

 

class Battle(object):

   def do_battle(self, hero, enemy):

       print("=====================")

       print("Hero faces the {}".format(enemy.name))

       print("=====================")

       while hero.alive() and enemy.alive():

           hero.print_status()

            enemy.print_status()

           time.sleep(1.5)

           print("-----------------------")

           print("What do you want to do?")

           print("1. fight {}".format(enemy.name))

           print("2. do nothing")

           print("3. flee")

           print("> ", end=' ')

           keyinput = int(input())

           if keyinput == 1:

               hero.attack(enemy)

           elif keyinput == 2:

               pass

           elif keyinput == 3:

               print("Goodbye.")

               exit(0)

           else:

               print("Invalid input {}".format(input))

               continue

           enemy.attack(hero)

       if hero.alive():

           print("You defeated the {}".format(enemy.name))

           return True

       else:

           print("YOU LOSE!")

           return False

 

class Tonic(object):

   cost = 5

   name = 'tonic'

   def apply(self, character):

       character.health += 2

       print("{}'s health increased to {}.".format(character.name, character.health))

 

class Sword(object):

   cost = 10

   name = 'sword'

   def apply(self, hero):

       hero.power += 2

       print("{}'s power increased to {}.".format(hero.name, hero.power))

 

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

               print("{}. buy {} ({})".format(i + 1, item.name, item.cost))

           print("10. leave")

           input = int(input("> "))

           if input == 10:

               break

            else:

               ItemToBuy = Store.items[input - 1]

               item = ItemToBuy()

               hero.buy(item)

 

if __name__ == "__main__":

   hero = Hero()

   enemies = [Goblin(), Wizard()]

   battle_engine = Battle()

   shopping_engine = Store()

 

   for enemy in enemies:

       hero_won = battle_engine.do_battle(hero, enemy)

       if not hero_won:

           print("YOU LOSE!")

           exit(0)

       shopping_engine.do_shopping(hero)

 

   print("YOU WIN!")

 