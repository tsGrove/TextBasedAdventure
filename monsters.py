import random

class Monster:
    def __init__(self,  hit_points=None, armor=None, attack=None, speed=None, name=''):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.name = name

    def __str__(self):
        return str(self.name)

class Goblin(Monster):
    def __init__(self, hit_points=5, armor=8, attack=4, speed=8, name=''):
        super().__init__(hit_points, armor, attack, speed, name)
        self.race = 'Goblin'



class Skeleton(Monster):
    def __init__(self, hit_points=8, armor=5, attack=4, speed=2, name=''):
        super().__init__(hit_points, armor, attack, speed, name)
        self.race = 'Skeleton'



class Troll(Monster):
    def __init__(self, hit_points=12, armor=12, attack=10, speed=6, name=""):
        super().__init__(hit_points, armor, attack, speed, name)
        self.race = 'Troll'


def generate_monster(monster_to_be_made):
        random_monster = monster_list[random.randint(0, 2)]
        monster_to_be_made = MONSTER_DICT[random_monster]
        print(monster_to_be_made.race)
        monster_to_be_made.name = (MONSTER_NAMES[random_monster][random.randint(0, (len(MONSTER_NAMES[random_monster])-1))])
        print(monster_to_be_made.name)
        return monster_to_be_made


def generate_monster_name(random_monster):
    random_name = (MONSTER_NAMES[random_monster][random.randint(0, (len(MONSTER_NAMES[random_monster])-1))])
    return random_monster(name=random_name)

random_baddie = Monster()

MONSTER_DICT = {
                'Goblin' : Goblin(),
                'Skeleton' : Skeleton(),
                'Troll' : Troll(),
                }

monster_list = ['Goblin', 'Skeleton', 'Troll']

MONSTER_NAMES = { "Troll" : ['Terry', 'Theodore', 'Trall', 'Timb'],
                  "Skeleton" : ['DICK', 'HARRY', 'RIBBED', 'Jesus Christ in the Flesh'],
                  "Goblin" : ['Harry', 'Balls', 'kekw']
}

generate_monster(random_baddie)
print(random_baddie.hit_points)
