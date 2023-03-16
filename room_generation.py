from actions import combat
from merchant import *
from dialogue import *

POSSIBLE_ENCOUNTERS = ['Monster', 'Monster', 'Monster', 'Monster', 'Treasure', 'Merchant', 'Trap', 'Trap']

def generate_room():
    room_contents = POSSIBLE_ENCOUNTERS[random.randint(0, len(POSSIBLE_ENCOUNTERS)-1)]
    if room_contents == 'Monster':
        combat(player_character)

    elif room_contents == 'Treasure':
        gold_found = random.randint(5, 10)
        print(TREASURE_FOUND_DIALOGUE[random.randint(0, (len(TREASURE_FOUND_DIALOGUE) - 1))])
        print(f"You found {gold_found} gold, nice!\n")
        player_character.gold += gold_found

    elif room_contents == 'Merchant':
        print('Hm? You can hear footsteps approaching from around the corner, you ready yourself for...\n')
        generate_merchant()

    else:
        print(POSSIBLE_TRAPPED_ROOM_DIALOGUE[random.randint(0, (len(POSSIBLE_TRAPPED_ROOM_DIALOGUE) - 1))])
        trap_chance = random.randint(0,20)
        if trap_chance >= 6:
            trapped_room()
        else:
            print(NO_TRAPS_DIALOGUE[random.randint(0, (len(NO_TRAPS_DIALOGUE) - 1))])

def player_choice():
    choice = input('What would you like to do?\n'
                   '(N)ext room, Use a/n (I)tem, Check your (S)tats, or (R)est?\n').lower()

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
                    print(POTION_DRANK_DIALOGUE[random.randint(0, (len(POTION_DRANK_DIALOGUE) - 1))])

                elif potion_choice == 'n' or potion_choice == 'no':
                    print('Fair enough, better to save it!')

                else:
                    print('Please enter a valid selection of yes, or no.')
                player_choice()

    elif choice == 'n' or choice == 'next':
        generate_room()

    elif choice == 's' or choice == 'stats':
        print(f"{player_character.name},\n"
              f"Currently have {player_character.hit_points} hit points,\n"
              f"Attack:{player_character.attack}, Armor:{player_character.armor}, Speed:{player_character.speed}")

    elif choice =='r' or choice == 'rest':

        encounter_chance = random.randint(0, 20)
        if encounter_chance >= 7:
            print('You hear something approaching you in the darkness...\n')
            combat(player_character)
        else:
            print(WELL_RESTED_DIALOGUE[random.randint(0, (len(WELL_RESTED_DIALOGUE) - 1))])
            player_character.hit_points = player_character.max_hit_points
    else:
        print("I'm sorry, you wanted to do what?\n")

def trapped_room():
    trap_difficulty_check = 13

    if random.randint(0, player_character.speed) + player_character.level > trap_difficulty_check:
        print(DODGED_TRAPPED_ROOM_DIALOGUE[random.randint(0, (len(DODGED_TRAPPED_ROOM_DIALOGUE) - 1))])

    else:
        damage = random.randint(1, 3)
        player_character.hit_points -= damage
        print(HIT_TRAPPED_ROOM_DIALOGUE[random.randint(0, (len(HIT_TRAPPED_ROOM_DIALOGUE) - 1))])
        print(f"You took {damage} damage.\n")

