# TODO Develop inventory, likely using dict
# TODO Work on item classes
# TODO Develop merchant NPC
# TODO Add exp drops to monsters so PC can level up
# TODO Add harder enemies, multiple levels of difficulty as PC levels up

from room_generation import player_choice
from classes import player_character
from merchant import generate_item

while player_character.hit_points > 0:
    generate_item()
    generate_item()
    print(player_character.hit_points)
    print(player_character.inventory)
    player_choice()


