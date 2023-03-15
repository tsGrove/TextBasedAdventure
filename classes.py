import random


class PlayerClass:
    def __init__(self, hit_points, armor, attack, speed, name,
                 gold, level, max_hit_points, monsters_slain, experience_points, exp_needed_to_level):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.inventory = {}
        self.name = name
        self.gold = gold
        self.level = level
        self.max_hit_points = max_hit_points
        self.monsters_slain = monsters_slain
        self.experience_points = experience_points
        self.exp_needed_to_level = exp_needed_to_level

    def __str__(self):
        return str(self.name)

    def level_up(self):
        if self.experience_points >= self.exp_needed_to_level:
            self.max_hit_points += 4
            self.hit_points += 4
            self.armor += 2
            self.attack += 2
            self.speed += 1
            self.experience_points = 0
            self.exp_needed_to_level += 15
            self.level += 1
            print(f"Congrats! You reached level {self.level}.")

class Fighter(PlayerClass):
    def __init__(self, hit_points=15, armor=14, attack = 13, speed=10, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=15, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)

    def greetings(self):
        return str(f"Greetings, {self.name} the Fighter, and welcome to the Dungeon!\n")


class Rogue(PlayerClass):
    def __init__(self, hit_points=13, armor=16, attack = 14, speed=15, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=13, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Rogue, and welcome to the Dungeon!\n")


class Wizard(PlayerClass):
    def __init__(self, hit_points=13, armor=11, attack = 16, speed=13, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=13, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Wizard, and welcome to the Dungeon!\n")


class Ranger(PlayerClass):
    def __init__(self, hit_points=13, armor=18, attack = 12, speed=16, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=13, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Ranger, and welcome to the Dungeon!\n")


CLASSES_DICT = {
                'Fighter' : Fighter(),
                'Wizard' : Wizard(),
                'Ranger' : Ranger(),
                'Rogue' : Rogue()
                }

player_class = input("What class would you like to play?\n").title()
player_name = input('What would you like this character to be called?\n').title()

if player_class in CLASSES_DICT:
    player_character = CLASSES_DICT[player_class]
    player_character.name = player_name
    print(player_character.greetings())

else:
    print('Please enter a valid class.')

class Item:
    def __init__(self, name='', attribute='', buy_value=0, sell_value=0, description=''):
        self.name = name
        self.attribute = attribute
        self.buy = buy_value
        self.sell = sell_value
        self.description = description

class Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Blade of Sharpness'
        self.description = 'A fairly sharp blade, increasing your attack by one.'
        self.buy = 20
        self.sell = 10

    def __call__(self, *args, **kwargs):
            return self

class Armor(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Superior Armor'
        self.description = 'A set of sturdy leather armor, making you more resilient against monster attacks'
        self.buy = 20
        self.sell = 8

    def __call__(self, *args, **kwargs):
            return self

class Boots(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Boots of Swiftness'
        self.description = 'A pair of boots increasing your speed, making it more likely for you to dodge traps'
        self.buy = 13
        self.sell = 6

    def __call__(self, *args, **kwargs):
        return self

class HealthPotion(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Potion of Healing'
        self.description = 'A bright red beverage, slightly bubbling in a crystal vial. Smells of cherry.'
        self.buy = 50
        self.sell = 10

    def __call__(self, *args, **kwargs):
        return self

    def drink_potion(self):
        self.attribute = player_character.health_points = player_character.max_hit_points

