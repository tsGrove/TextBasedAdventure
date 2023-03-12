import random
from classes import *

ITEM_TYPES = ['Weapon', 'Potion']

def generate_item():
    item_choice = ITEM_TYPES[random.randint(0, (len(ITEM_TYPES) - 1))]
    if item_choice == 'Weapon':
        weapon = Sword()
        player_character.inventory[weapon.name] = weapon.description
        player_character.attack += 1

    elif item_choice == 'Potion':
        health_potion = HealthPotion()
        player_character.inventory[health_potion.name] = health_potion.description

