# Player Classes -------------------------------------------------------------------------------------------------------
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
            self.exp_needed_to_level = (self.level * 10)
            self.level += 1
            print(f"Congrats! You reached level {self.level}!")

class Fighter(PlayerClass):
    def __init__(self, hit_points=10, armor=10, attack =3, speed=3, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=10, level=1, max_hit_points=10, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)

    def greetings(self):
        return str(f"Greetings, {self.name} the Fighter, and welcome to the Text-geon!\n")


class Rogue(PlayerClass):
    def __init__(self, hit_points=8, armor=10, attack =3, speed=5, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=8, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Rogue, and welcome to the Text-geon!\n")


class Wizard(PlayerClass):
    def __init__(self, hit_points=6, armor=6, attack =8, speed=3, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=6, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Wizard, and welcome to the Text-geon!\n")


class Ranger(PlayerClass):
    def __init__(self, hit_points=10, armor=10, attack = 3, speed=5, name=''):
        super().__init__(hit_points, armor, attack, speed, name,
                         gold=0, level=1, max_hit_points=10, monsters_slain=0, experience_points=0, exp_needed_to_level= 10)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Ranger, and welcome to the Text-geon!\n")


CLASSES_DICT = {
                'Fighter' : Fighter(),
                'Wizard' : Wizard(),
                'Ranger' : Ranger(),
                'Rogue' : Rogue()
                }

# Creation of Character -----------------------------------------------------------------------------------------------

print("Welcome to the Text-geon, a text based, randomly generated dungeon-crawl.\n"
      "Here are a list of playable classes:\n"
      "Fighter: Average across the board. Doesn't excel in any particular area, nor does he suffer. \n"
      "Rogue: Nimble in the shadows, the Rogue has high speed, average attack, average armor, below average HP. \n"
      "Wizard: Spellbook in hand, the Wizard is a glass canon. High attack, average speed, below average HP, below average armor.\n"
      "Ranger: Slow and steady wins the race. the Ranger is methodical in these dungeons. High Speed, High Armor, Average HP, low attack.\n")
player_class = input("What class would you like to play?\n").title()
player_name = input('What would you like this character to be called?\n').title()

if player_class in CLASSES_DICT:
    player_character = CLASSES_DICT[player_class]
    player_character.name = player_name
    print(player_character.greetings())

else:
    print('Please enter a valid class.')
