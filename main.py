# TODO Add more item types
# TODO Set Custom level up stats for different classes

from helper_functions.room_generation import player_choice
from player_character.player_info import player_character
from helper_functions.combat import game_over

while player_character.hit_points > 0:
    player_choice()

else:
    game_over(player_character)

