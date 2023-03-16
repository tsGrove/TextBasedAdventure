import random
from monsters import *

def player_attack(player, target):
    if random.randint(0,20) + round(player.attack/10) > target.armor:

        damage = random.randint(1, 6) + player.attack
        target.hit_points -= damage
        return f"You hit {target.name} for {damage}!\n"

    else:
        return f"Unfortunately you missed {target.name}, try again!\n"

def monster_attack(monster, player):
    if random.randint(0,20) + (monster.attack/10) > player.armor:

        damage = random.randint(1, 6) + monster.attack
        player.hit_points -= damage
        return f"{monster.name} hit you for {damage} damage!\n"

    else:

        return f"{monster.name} missed! close one!\n"

def combat(player):
    encounter = True

    monster_race = EASY_MONSTER_LIST[random.randint(0, (len(EASY_MONSTER_LIST) - 1))]
    monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, int(len(MONSTER_NAMES_DICT[monster_race]) - 1))]
    monster = EASY_MONSTERS_DICT[monster_race]
    monster.name = monster_name

    print(monster.intro)
    print(f"Look out! Its {monster.name} the {monster.race}!")

    while encounter:

        player_choice = input("What would you like to do? \n(A)ttack, or (R)un?\n").lower()
        if player_choice == 'attack' or player_choice == 'a':

           print(player_attack(player, monster))
           print(monster_attack(monster, player))

           if monster.hit_points > 0 and player.hit_points > 0:
               continue

           elif monster.hit_points <= 0 < player.hit_points:

               encounter = False
               print(f"You defeated {monster}.\n")
               player.monsters_slain += 1
               gold_drop(player, monster)
               player.experience_points += monster.exp_yield
               player.level_up()
               monster.hit_points = monster.max_hit_points

           elif player.hit_points <= 0 < monster.hit_points:

               encounter = False
               print(f"{monster} defeated you! Oh no! Better luck next time\n")
               game_over(player)

           else:

               encounter = False
               print(f"My god! It would appear both {player.name} and {monster.name} killed each other at the same "
                     f"time! Oh well, lets grab {player.name}'s stuff and get out of here.\n")
               game_over(player)

        elif player_choice == 'run' or player_choice == 'r':

            run_chance = (random.randint(0, 20) + player.speed)

            if run_chance > monster.speed:

                print("You successfully escaped!\n")
                encounter = False

            else:

                 print(monster_attack(monster, player))

        else:

            print("Please enter a valid option, either 'Attack', or 'Run'.\n")


def gold_drop(player, monster):
    if monster.race in EASY_MONSTER_LIST:

        gold_dropped = random.randint(2, 10)
        player.gold += gold_dropped
        print(f"You found {gold_dropped} gold from {monster.name}! Swish!")

    return player.gold

def game_over(player):
    print(f'It was a good run {player.name}, but eventually you fell. \n'
          f'You slayed {player.monsters_slain} monsters, had {player.gold} gold, and reached level {player.level}!\n'
          f'Better luck next time!')

