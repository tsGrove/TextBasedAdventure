import random
from actions import combat
from main import player_character

POSSIBLE_ENCOUNTERS = ['Monster', 'Treasure', 'Merchant', 'Empty']

def generate_room():
    room_contents = random.randint(0, len(POSSIBLE_ENCOUNTERS)-1)
    if room_contents == 0:
        combat(player_character)
    elif room_contents == 1:
        gold_found = random.randint(10, 200)
        player_character.gold += gold_found
        print(f"You found {gold_found}, we're eating good tonight!")
    elif room_contents == 2:
        print('Hey, theres a wagon in this room? And some old guy selling wares?')
    else:
        print('Hmmm...this room seems quiet. You feel like something is off.')