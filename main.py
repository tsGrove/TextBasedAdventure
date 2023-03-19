# TODO Add more item types
# TODO Multiple levels of difficulty as PC levels up
# TODO Set Custom level up stats for different classes
# TODO Go over base stats of classes

from room_generation import player_choice
from player_info import player_character
from actions import game_over

while player_character.hit_points > 0:
    player_choice()

else:
    game_over(player_character)

