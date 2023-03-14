# TODO Work on item classes
# TODO Develop merchant NPC
# TODO Add exp drops to monsters so PC can level up
# TODO Add harder enemies, multiple levels of difficulty as PC levels up

from room_generation import player_choice
from classes import player_character

while player_character.hit_points > 0:
    player_choice()


