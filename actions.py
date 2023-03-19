import random
from monsters import *
from dialogue import COMBAT_ESCAPE_DIALOGUE

def random_element_from_list(custom_list):
    random_selection = custom_list[random.randint(0, (len(custom_list) - 1))]
    return random_selection


def player_attack(player, target):
    if random.randint(1, 20) + player.attack > target.armor:

        damage = random.randint(1, 6) + player.attack
        target.hit_points -= damage
        return f"You hit {target.name} for {damage}!\n"

    else:
        return f"Unfortunately you missed {target.name}, try again!\n"


def monster_attack(monster, player):
    if random.randint(1, 20) > player.armor:

        damage = random.randint(1, 6) + monster.attack
        player.hit_points -= damage
        return f"{monster.name} hit you for {damage} damage!\n"

    else:

        return f"{monster.name} missed! close one!\n"


def combat(player):
    encounter = True

    if player.level <= 3:
        monster_race = random_element_from_list(EASY_MONSTER_LIST)
        monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, int(len(MONSTER_NAMES_DICT[monster_race]) - 1))]
        monster = MONSTERS_DICT[monster_race]
        monster.name = monster_name

    elif 3 < player.level <= 6:
        monster_race = random_element_from_list(MEDIUM_MONSTER_LIST)
        monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, (len(MONSTER_NAMES_DICT[monster_race]) - 1))]
        monster = MONSTERS_DICT[monster_race]
        monster.name = monster_name

    elif 6 < player.level <= 9:
        monster_race = random_element_from_list(HARD_MONSTER_LIST)
        monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, (len(MONSTER_NAMES_DICT[monster_race]) - 1))]
        monster = MONSTERS_DICT[monster_race]
        monster.name = monster_name

    else:
        monster_race = random_element_from_list(BOSS_MONSTER_LIST)
        monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, (len(MONSTER_NAMES_DICT[monster_race]) - 1))]
        monster = MONSTERS_DICT[monster_race]
        monster.name = monster_name

    player_turn = random.randint(1, 20) + player.speed
    monster_turn = random.randint(1, 20) + monster.speed

    if player_turn > monster_turn:

        turn_order = [player, monster]

    else:
        turn_order = [monster, player]

    print(monster.intro)
    print(f"Look out! Its {monster.name} the {monster.race}!")

    while encounter:

        player_choice = input("What would you like to do? \n(A)ttack, or (R)un?\n").lower()
        if player_choice == 'attack' or player_choice == 'a':

            if turn_order[0] == monster:
                print(monster_attack(monster, player))

                if player.hit_points > 0:
                    print(player_attack(player, monster))

                    if monster.hit_points <= 0:
                        encounter = False
                        print(f"You defeated {monster.name}.\n")
                        player.monsters_slain += 1
                        gold_drop(player, monster)
                        player.experience_points += monster.exp_yield
                        player.level_up()
                        monster.hit_points = monster.max_hit_points

                else:
                    encounter = False
                    print(f"{monster} defeated you! Oh no! Better luck next time\n")
                    game_over(player)


            else:
                print(player_attack(player, monster))

                if monster.hit_points > 0:
                    print(monster_attack(monster, player))

                    if player.hit_points <= 0:
                        encounter = False
                        game_over(player)

                else:
                    encounter = False
                    print(f"You defeated {monster.name}.\n")
                    player.monsters_slain += 1
                    gold_drop(player, monster)
                    player.experience_points += monster.exp_yield
                    player.level_up()
                    monster.hit_points = monster.max_hit_points

        elif player_choice == 'run' or player_choice == 'r':

            run_chance = (random.randint(1, 20) + player.speed)

            if run_chance > monster.speed:

                print(random_element_from_list(COMBAT_ESCAPE_DIALOGUE))
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

    elif monster.race in MEDIUM_MONSTER_LIST:
        gold_dropped = random.randint(10, 50)
        player.gold += gold_dropped
        print(f"Wow, {monster.name} had {gold_dropped} gold in his pocket! Nice.")

    elif monster.race in HARD_MONSTER_LIST:
        gold_dropped = random.randint(50, 150)
        player.gold = gold_dropped
        print(f"{gold_dropped} gold from the {monster.race}!! You're rich!!")

    else:
        gold_dropped = random.randint(1000, 10000)
        player.gold = gold_dropped
        print(f"With {monster.name} the {monster.race} finally slain, you find {gold_dropped} gold in his treasure.\n"
              f"You could retire for life!")

    return player.gold


def game_over(player):
    if player.monsters_slain <= 1:
        print('Cmon you can definitely do better than ONE or ZERO monsters...right?\n'
              f'The mighty {player.name} slayed a whopping {player.monsters_slain} monsters, wow! \n'
              f'Better luck next time!')

    print(f'It was a good run {player.name}, but eventually you fell. \n'
          f'You slayed {player.monsters_slain} monsters, had {player.gold} gold, and reached level {player.level}!\n')
    input()
