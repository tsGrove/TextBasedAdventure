import random
from classes import player_character
from actions import combat

POSSIBLE_ENCOUNTERS = ['Monster', 'Treasure', 'Merchant', 'Trap']
def generate_room():
    room_contents = POSSIBLE_ENCOUNTERS[random.randint(0, len(POSSIBLE_ENCOUNTERS)-1)]

    if room_contents == 'Monster':
        combat(player_character)
        player_choice()

    elif room_contents == 'Treasure':
        gold_found = random.randint(5, 30)
        print('Theres something shiny in the corner there...\n')
        print(f"You found {gold_found} gold, nice!\n")
        player_choice()

    elif room_contents == 'Merchant':
        print('Hey, theres a wagon in this room? And some old guy selling wares?\n')
        player_choice()

    else:
        print('Hmmm...this room seems quiet. You feel like something is off.\n')
        trap_chance = random.randint(0,20)
        if trap_chance >= 6:
            trapped_room()

        player_choice()

def player_choice():
    choice = input('What would you like to do?\n'
                   'Use a/n (I)tem, (N)ext room, or (R)est?\n').lower()

    if choice == 'item' or choice == 'i':
        print('This is a place holder until I do items :0)\n')
        player_choice()

    elif choice == 'n' or choice == 'next room':
        generate_room()

    elif choice =='r' or choice == 'rest':

        encounter_chance = random.randint(0, 20)
        if encounter_chance >= 14:
            print('You hear something approaching you in the darkness...\n')
            combat(player_character)
        else:
            print('You feel well rested!\n')
            player_character.hit_points = player_character.max_hit_points
    else:
        print("I'm sorry, you wanted to do what?\n")
        player_choice()

def trapped_room():
    trap_difficulty_check = 13

    if random.randint(0, player_character.speed) + player_character.level > trap_difficulty_check:
        print('Oh man that was a close one! There were some floor spikes down there!\n')

    else:
        damage = random.randint(0, 6)
        player_character.hit_points -= damage
        print(f"Ouch! There were some spikes hidden in the floor, you took {damage} damage.\n")

