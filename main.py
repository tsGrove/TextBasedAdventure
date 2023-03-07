# TODO GENERATE RANDOM ENCOUNTER
# TODO Combat actions, attack, run, use item
# TODO Develop inventory, likely using dict
# TODO Exploration Actions
from actions import combat
from classes import classes_dict

player_class = input("What class would you like to play?\n").title()
player_name = input('What would you like this character to be called?\n').title()

if player_class in classes_dict:
    player_character = classes_dict[player_class]
    player_character.name = player_name
    print(player_character.greetings())

    while player_character.hit_points > 0:
        combat(player_character)




