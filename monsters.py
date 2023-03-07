MONSTER_LIST = ['Goblin', 'Skeleton', 'Troll']
MONSTER_NAMES_DICT = {
                "Troll" : ['Terry', 'Theodore', 'Trall', 'Timb'],
                "Skeleton" : ['DICK', 'HARRY', 'RIBBED', 'Jesus Christ in the Flesh'],
                "Goblin" : ['Harry', 'Balls', 'kekw']
                }

class Monster:
    def __init__(self, name='', race='', attack=0, hit_points=0, speed=0):
        self.name = name
        self.race = race
        self.attack = attack
        self.hit_points = hit_points
        self.speed = speed

    def __str__(self):
        return str(self.name)

class Goblin(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Goblin'
        self.attack = 50
        self.armor = 8
        self.hit_points = 8
        self.speed = 12

    def __call__(self, *args, **kwargs):
        return self

class Troll(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Troll'
        self.attack = 100
        self.armor = 7
        self.hit_points = 13
        self.speed = 10

    def __call__(self, *args, **kwargs):
        return self

class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Skeleton'
        self.attack = 70
        self.armor = 6
        self.hit_points = 6
        self.speed = 5

    def __call__(self, *args, **kwargs):
        return self

MONSTERS_DICT = {
                'Goblin' : Goblin(),
                'Troll' : Troll(),
                'Skeleton' : Skeleton()
}