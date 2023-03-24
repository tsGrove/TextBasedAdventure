import json
import random
from monsters import *
from dialogue import COMBAT_ESCAPE_DIALOGUE

# Grabs a random element from a list, used in a lot of the random options generated throughout the program
def random_element_from_list(custom_list):
    random_selection = custom_list[random.randint(0, (len(custom_list) - 1))]
    return random_selection


# Rolls a random integer between 1 and 20, if said number + the players attack is higher than the monsters defense,
# The attack is successful
def player_attack(player, monster):
    if random.randint(1, 20) + player.attack > monster.armor:

        damage = random.randint(1, 6) + round(player.attack / 2)
        monster.hit_points -= damage
        return f"You hit {monster.name} for {damage}!\n"

    else:
        return f"Unfortunately you missed {monster.name}, try again!\n"

# Same for player attack but i wanted different text for each side so it didnt get boring to read.
def monster_attack(monster, player):
    if random.randint(1, 20) > player.armor:

        damage = random.randint(1, 6) + round(monster.attack / 2)
        player.hit_points -= damage
        return f"{monster.name} hit you for {damage} damage!\n"

    else:

        return f"{monster.name} missed! close one!\n"

# Combat starts by generating a monster object from a dictionary based on characters level, from there the turn order
# Is decided based on a random integer + plus each respective objects speed, player and monster. From there the player is given
# Two options, to run or to attack. If attack is selected, then they go in order with HP values being checked at the end of
# Each function, if the monster is slain the player is awarded gold and experience, if the monsters stands the while loop continues
# And if the player falls they are given a game over message telling them to get good
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


# A random amount of gold is generated and given to the player based on the difficulty of the monster they just faced
# And defeated
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


# After the game ends the current run is written into a json file, for the player to look at and admire past attempts
# Tracking stats such as level reached, gold earned, and monsters slain. The dict will be sorted by level reached, and will
# Display the top 10 characters using a tables library i need to install
def game_over(player):

    addition_to_high_score = {
        "name": str(player.name),
        "level reached" : int(player.level),
        "monsters slain" : int(player.monsters_slain),
        "gold earned" : int(player.gold)
                 }

    if player.monsters_slain <= 1:
        print('Cmon you can definitely do better than ONE or ZERO monsters...right?\n'
              f'The mighty {player.name} slayed a whopping {player.monsters_slain} monsters, wow! \n'
              f'Better luck next time!')

    else:
        print(f'It was a good run {player.name}, but eventually you fell. \n'
              f'You slayed {player.monsters_slain} monsters, had {player.gold} gold, and reached level {player.level}!\n')

    with open("json_scores.json", "r+") as file:
        file_data = json.load(file)
        file_data["High Scores"].append(addition_to_high_score)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    check_high_scores()
    input()

# This just reads the json file and returns the data if the user so wishes to see it
def check_high_scores():
    check_scores = input('Would you like to see your top 10 high scores?\n').lower()
    if check_scores == "yes" or check_scores == 'y':
        with open("json_scores.json", 'r') as f:
            data = json.load(f)
            for player in data['High Scores']:
                print(f"Adventurer Name: {player['name']}, Level: {player['level reached']}, Gold Earned: {player['gold earned']}, Number of Monsters Slain: {player['monsters slain']}")
    else:
        print('Gotcha, Hope you\'re brave enough to try again!')