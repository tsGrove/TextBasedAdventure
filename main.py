# TODO Add more item types
# TODO Set Custom level up stats for different classes

from room_generation import player_choice
from player_info import player_character
from actions import game_over

while player_character.hit_points > 0:
    player_choice()

else:
    game_over(player_character)

