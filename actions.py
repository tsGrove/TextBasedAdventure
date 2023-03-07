import random
from monsters import *

def attack_enemy(player, target):
    if random.randint(0,20) + (player.attack/10) > target.armor:
        damage = random.randint(1, 6) + player.attack
        target.hit_points -= damage
        return f"You hit {target.name} for {damage}!"
    else:
        return f"Unfortunately you missed {target.name}, try again!"

def combat(player):
    encounter = True

    MONSTER_RACE = MONSTER_LIST[random.randint(0, (len(MONSTER_LIST) - 1))]
    MONSTER_NAME = MONSTER_NAMES_DICT[MONSTER_RACE][random.randint(0, int(len(MONSTER_NAMES_DICT[MONSTER_RACE]) - 1))]
    monster = MONSTERS_DICT[MONSTER_RACE]
    monster.name = MONSTER_NAME

    while encounter:

        print(player.hit_points)
        print(f"Oh shit, theres {monster.name}, the {monster.race}!")
        player_choice = input('What would you like to do? \n'
                              'Attack, or run?\n').lower()

        if player_choice == 'attack':
           print(attack_enemy(player, monster))
           print(attack_enemy(monster, player))

           if monster.hit_points > 0 and player.hit_points > 0:
               continue

           elif monster.hit_points <= 0 <= player.hit_points:
               encounter = False
               print(f"You defeated {monster}")

           elif player.hit_points <= 0 <= monster.hit_points:
               encounter = False
               print(f"{monster} defeated you! Oh no! Better luck next time")

           else:
               encounter = False
               print(f"My god! It would appear both {player.name} and {monster.name} killed each other at the same "
                     f"time! Oh well, lets grab {player.name}'s stuff and get out of here.")

        elif player_choice == 'run':
            run_chance = (random.randint(0, 20) + player.speed)

            if run_chance > monster.speed:
                print("You successfully escaped!")
                encounter = False

            else:
                 print(attack_enemy(monster, player))

        else:
            print("Please enter a valid option, either 'Attack', or 'Run'.")