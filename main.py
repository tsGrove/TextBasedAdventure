## Main Game Loop

from functionality.room_generation import player_choice
from player_character.player_info import player_character
from functionality.game_over import game_over

while player_character.hit_points > 0:
    game_loop = True
    while game_loop:
        player_choice()

else:
    game_loop = False
    game_over(player_character)
    exit()
