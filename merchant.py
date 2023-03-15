import random
from classes import Sword, Armor, Boots, HealthPotion, player_character

ITEM_TYPES = ['Weapon', 'Potion', 'Armor', 'Boots']

ITEM_DICT = {
            'Weapon' : Sword(),
            'Potion' : HealthPotion(),
            'Armor' : Armor(),
            'Boots' : Boots(),
            }

def generate_merchant():
    print("An old man approaches from the cart, the torch light behind him makes it hard to see his face as he calls out,\n"
          "'Greetings adventurer, you look like you could use an extra edge here in the dungeon, have a look at my "
          "goods?'")

    shop_or_not = input('Would you like to see what item the old man has for sale? (Y)es, or (n)o.\n').lower()

    if shop_or_not == 'yes' or shop_or_not == 'y':
        random_item = ITEM_TYPES[random.randint(0, (len(ITEM_TYPES) - 1))]
        item_choice = ITEM_DICT[random_item]

        print(f'Most excellent! Today for you I have a {item_choice.name}, which is {item_choice.description},'
              f' for the low, low price of {item_choice.buy} gold. Are you interested?')
        buy_or_pass = input(f'Would you like to spend {item_choice.name} for {item_choice.buy} gold? (Y)es or (n)o.\n'
                            f'You currently have {player_character.gold} gold.\n').lower()

        if buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold > item_choice.buy:

            print('How generous of you! Here you are!')
            print(f"{item_choice.name} acquired!")
            player_character.gold -= item_choice.buy
            player_character.inventory[item_choice.name] = item_choice.description

            if item_choice == 'Weapon':
                player_character.attack += 1

            if item_choice == 'Armor':
                player_character.armor += 1

            if item_choice == 'Boots':
                player_character.speed += 1

        elif buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold < item_choice.buy:
            print('Oh no! I dont believe you have enough gold friend. Maybe we\'ll see each other again!')

        elif buy_or_pass == 'no' or buy_or_pass == 'n':
            print('Understandable! Hopefully i can return with something that will appease you.')

        else:
            print('Im sorry? I couldn\'t hear you over the monsters screaming')







