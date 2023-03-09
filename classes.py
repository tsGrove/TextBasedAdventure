# Player Classes
class PlayerClass:
    def __init__(self, hit_points, armor, attack, speed, name, gold, level, max_hit_points):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.inventory = {}
        self.name = name
        self.gold = gold
        self.level = level
        self.max_hit_points = max_hit_points

    def __str__(self):
        return str(self.name)

class Fighter(PlayerClass):


    def __init__(self, hit_points=15, armor=14, attack = 13, speed=10, name=''):
        super().__init__(hit_points, armor, attack, speed, name, gold=0, level=1, max_hit_points=15)

    def greetings(self):
        return str(f"Greetings, {self.name} the Fighter, and welcome to the Dungeon!\n")

class Rogue(PlayerClass):
    def __init__(self, hit_points=13, armor=20, attack = 14, speed=15, name=''):
        super().__init__(hit_points, armor, attack, speed, name, gold=0, level=1, max_hit_points=13)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Rogue, and welcome to the Dungeon!\n")

class Wizard(PlayerClass):
    def __init__(self, hit_points=13, armor=13, attack = 16, speed=13, name=''):
        super().__init__(hit_points, armor, attack, speed, name, gold=0, level=1, max_hit_points=13)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Wizard, and welcome to the Dungeon!\n")

class Ranger(PlayerClass):
    def __init__(self, hit_points=13, armor=22, attack = 13, speed=16, name=''):
        super().__init__(hit_points, armor, attack, speed, name, gold=0, level=1, max_hit_points=13)
        self.inventory = {}

    def greetings(self):
        return str(f"Greetings, {self.name} the Ranger, and welcome to the Dungeon!\n")

classes_dict = {
                'Fighter' : Fighter(),
                'Wizard' : Wizard(),
                'Ranger' : Ranger(),
                'Rogue' : Rogue()
                }