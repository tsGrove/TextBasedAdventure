from player_character.player_info import player_character
from player_character.items import Sword, Armor, Boots, HealthPotion
from functionality.dialogue import MERCHANT_DIALOGUE_LIST
from functionality.combat import random_element_from_list

ITEM_TYPES = ['Weapon', 'Potion', 'Armor', 'Boots']

ITEM_DICT = {
            'Weapon' : Sword(),
            'Potion' : HealthPotion(),
            'Armor' : Armor(),
            'Boots' : Boots(),
            }

def generate_merchant():
    print(random_element_from_list(MERCHANT_DIALOGUE_LIST))
    shop_or_not = input('Would you like to see what item the merchant has for sale? (Y)es, or (n)o.\n').lower()
    if shop_or_not == 'n' or shop_or_not == 'no':
        print(shop_or_not)

    elif shop_or_not == 'yes' or shop_or_not == 'yes':
        print(f'Most excellent! Today for you I have a {item_choice.name}, which is {item_choice.description},'
                  f' for the low, low price of {item_choice.buy} gold. Are you interested?')
        shopping = True
        while shopping:
            buy_or_pass = input(
                f'Would you like to spend {item_choice.name} for {item_choice.buy} gold? (Y)es or (n)o.\n'
                                    f'You currently have {player_character.gold} gold.\n').lower()

            ## If character has enough gold and says yes, trade is successful
            if buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold > item_choice.buy:
                print('How generous of you! Here you are!')
                print(f"{item_choice.name} acquired!")
                player_character.gold -= item_choice.buy
                player_character.inventory[item_choice.name] = item_choice.description
                if random_item == 'Weapon':
                    player_character.attack += 1
                if random_item == 'Armor':
                    player_character.armor += 1
                if random_item == 'Boots':
                    player_character.speed += 1
                shopping = False

            ## If character says yes, but doesn't have enough gold
            if buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold < item_choice.buy:
                print('Oh no! I dont believe you have enough gold friend. Maybe we\'ll see each other again!')
                shopping = False

            ## If character is not interested in item
            if buy_or_pass == 'no' or buy_or_pass == 'n':
                print('Understandable! Hopefully i can return with something that will appease you.')
                shopping = False











    # if shop_or_not == 'yes' or shop_or_not == 'y':
    #     shopping = True
    #     random_item = random_element_from_list(ITEM_TYPES)
    #     item_choice = ITEM_DICT[random_item]
    #     print(f'Most excellent! Today for you I have a {item_choice.name}, which is {item_choice.description},'
    #           f' for the low, low price of {item_choice.buy} gold. Are you interested?')
    #     buy_or_pass = input(f'Would you like to spend {item_choice.name} for {item_choice.buy} gold? (Y)es or (n)o.\n'
    #                         f'You currently have {player_character.gold} gold.\n').lower()
    #     if buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold > item_choice.buy:
    #         print('How generous of you! Here you are!')
    #         print(f"{item_choice.name} acquired!")
    #         player_character.gold -= item_choice.buy
    #         player_character.inventory[item_choice.name] = item_choice.description
    #         shopping = False
    #         if random_item == 'Weapon':
    #             player_character.attack += 1
    #         if random_item == 'Armor':
    #             player_character.armor += 1
    #         if random_item == 'Boots':
    #             player_character.speed += 1
    #     elif buy_or_pass == 'yes' or buy_or_pass == 'y' and player_character.gold < item_choice.buy:
    #         print('Oh no! I dont believe you have enough gold friend. Maybe we\'ll see each other again!')
    #         shopping = False
    #     elif buy_or_pass == 'no' or buy_or_pass == 'n':
    #         print('Understandable! Hopefully i can return with something that will appease you.')
    #         shopping = False
    #     else:
    #         print("Im sorry, I couldn't hear you over the monsters screaming, could you repeat that?\n"
    #               "Please enter (Y)es or (N)o.")
    #
    #
    #    elif shop_or_not == "no" or shop_or_not == 'n':
    #         print('Understandable, have an excellent adventure!')
    #         shopping = False
    #
    #     else:
    #         shop_or_not = input("Im sorry, I couldn't hear you over the monsters screaming, could you repeat that?\n"
    #               "Please enter (Y)es or (N)o.")


    ## Shopping flow chart
    ## Do you want to buy tiem?
