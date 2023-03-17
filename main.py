# TODO Add turn order based on player speed vs monster speed
# TODO Add more item types
# TODO Multiple levels of difficulty as PC levels up

from room_generation import player_choice
from player_info import player_character

while player_character.hit_points > 0:
    player_choice()



