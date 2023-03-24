import random
from actions import combat
from merchant import *
from dialogue import *

POSSIBLE_ENCOUNTERS = ['Monster', 'Monster', 'Monster', 'Monster', 'Treasure', 'Merchant', 'Trap', 'Trap']

# Generate room function firsts selects a random element from inside the Possible Encounters List, and then gives
# The player an encounter based on the element selected, ranging from Monster which starts the combat function, Treasure
# Which rolls for a random amount of gold, Merchant which spawns an npc selling a random item, and Trap which makes a
# Hidden check to see if a trap is in the next room or not

def generate_room():
    room_contents = random_element_from_list(POSSIBLE_ENCOUNTERS)
    if room_contents == 'Monster':
        combat(player_character)

    elif room_contents == 'Treasure':
        gold_found = random.randint(5, 10)
        print(random_element_from_list(TREASURE_FOUND_DIALOGUE))
        print(f"You found {gold_found} gold, nice!\n")
        player_character.gold += gold_found

    elif room_contents == 'Merchant':
        print('Hm? You can hear footsteps approaching from around the corner, you ready yourself for...\n')
        generate_merchant()

    else:
        print(random_element_from_list(POSSIBLE_TRAPPED_ROOM_DIALOGUE))
        trap_chance = random.randint(0,20)
        if trap_chance >= 6:
            trapped_room()
        else:
            print(random_element_from_list(NO_TRAPS_DIALOGUE))

# Player Choice gives the player 4 options to select from, ranging from Going to the next room, where a random event
# Is selected using Generate Room Function, Inventory, which returns the players inventory contents and gold amount,
# Stats, which allows players to check their current HP and other values, and Rest, where a player can attempt to
# Rest back to full at the risk of a monster spawning and negating their hp rejuvenation

def player_choice():
    choice = input("What would you like to do?\n"
                   "(N)ext room, Check (I)ventory, Check your (S)tats, or (R)est?\n").lower()

    if choice == 'item' or choice == 'i':
        print("In your pocket you've got,")
        print(f"{player_character.gold} gold jingling around,")

        for item in player_character.inventory:
            print(f"and {item}, {player_character.inventory[item]}")
            if 'Potion of Healing' in player_character.inventory:
                potion_choice = input('Would you like to drink a potion, (Y)es or (n)o?\n').lower()
                print(f"You currently have {player_character.hit_points}")

                if potion_choice == 'y' or potion_choice == 'yes':
                    health_potion = HealthPotion()
                    health_potion.drink_potion()
                    print(random_element_from_list(POTION_DRANK_DIALOGUE))

                elif potion_choice == 'n' or potion_choice == 'no':
                    print('Fair enough, better to save it!')

                else:
                    print('Please enter a valid selection of yes, or no.')
                player_choice()

    elif choice == 'n' or choice == 'next':
        generate_room()

    elif choice == 's' or choice == 'stats':
        print(f"{player_character.name},\n"
              f"You currently have {player_character.hit_points} of out {player_character.max_hit_points} hit points,\n"
              f"Attack:{player_character.attack}, Armor:{player_character.armor}, Speed:{player_character.speed}")

    elif choice =='r' or choice == 'rest':

        encounter_chance = random.randint(0, 20)
        if encounter_chance >= 10:
            print('You hear something approaching you in the darkness...\n')
            combat(player_character)
        else:
            print(random_element_from_list(WELL_RESTED_DIALOGUE))
            player_character.hit_points = player_character.max_hit_points
    else:
        print("I'm sorry, you wanted to do what?\n")

# Generates the chance of a trap being in a room a player enters, the higher the players speed the more likely
# They avoid said trap

def trapped_room():
    trap_difficulty_check = 13

    if random.randint(0, player_character.speed) + player_character.level > trap_difficulty_check:
        print(random_element_from_list(DODGED_TRAPPED_ROOM_DIALOGUE))

    else:
        damage = random.randint(1, 3)
        player_character.hit_points -= damage
        print(random_element_from_list(HIT_TRAPPED_ROOM_DIALOGUE))
        print(f"You took {damage} damage.\n")