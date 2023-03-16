from actions import combat
from merchant import *

POSSIBLE_ENCOUNTERS = ['Monster', 'Monster', 'Monster', 'Monster', 'Treasure', 'Merchant', 'Trap', 'Trap']
def generate_room():
    room_contents = POSSIBLE_ENCOUNTERS[random.randint(0, len(POSSIBLE_ENCOUNTERS)-1)]
    if room_contents == 'Monster':
        combat(player_character)

    elif room_contents == 'Treasure':
        gold_found = random.randint(5, 10)
        print('Theres something shiny in the corner there...\n')
        print(f"You found {gold_found} gold, nice!\n")
        player_character.gold += gold_found

    elif room_contents == 'Merchant':
        print('Hm? You can hear footsteps approaching from around the corner, you ready yourself for...\n')
        generate_merchant()

    else:
        print('Hmmm...this room seems quiet. You feel like something is off.\n')
        trap_chance = random.randint(0,20)
        if trap_chance >= 6:
            trapped_room()
        else:
            print("Huh, must've been the wind.")

def player_choice():
    choice = input('What would you like to do?\n'
                   'Use a/n (I)tem, (N)ext room, or (R)est?\n').lower()

    if choice == 'item' or choice == 'i':
        print("In your pocket you've got,")
        print(f"{player_character.gold} gold jingling around,")

        for item in player_character.inventory:
            print(f"and {item}, {player_character.inventory[item]}")
            if 'Potion of Healing' in player_character.inventory:
                potion_choice = input('Would you like to drink a potion, (Y)es or (n)o?\n').lower()

                if potion_choice == 'y' or potion_choice == 'yes':
                    health_potion = HealthPotion()
                    health_potion.drink_potion()
                    print('You feel refreshed and rejuvenated!')

                elif potion_choice == 'n' or potion_choice == 'no':
                    print('Alright alright alriiiiight')

                else:
                    print('Please enter a valid selection of yes, or no.')
                player_choice()

    elif choice == 'n' or choice == 'next room':
        generate_room()

    elif choice =='r' or choice == 'rest':

        encounter_chance = random.randint(0, 20)
        if encounter_chance >= 8:
            print('You hear something approaching you in the darkness...\n')
            combat(player_character)
        else:
            print('You feel well rested!\n')
            player_character.hit_points = player_character.max_hit_points
    else:
        print("I'm sorry, you wanted to do what?\n")

def trapped_room():
    trap_difficulty_check = 13

    if random.randint(0, player_character.speed) + player_character.level > trap_difficulty_check:
        print('Oh man that was a close one! There were some floor spikes down there! Good thing we didnt step on them.\n')

    else:
        damage = random.randint(1, 3)
        player_character.hit_points -= damage
        print(f"Ouch! There were some spikes hidden in the floor, you took {damage} damage.\n")

