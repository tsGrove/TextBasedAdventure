import random
MONSTER_NAME = ''
MONSTER_RACE = ''
MONSTER_LIST = ['Goblin', 'Skeleton', 'Troll']
MONSTER_NAMES_DICT = {
                "Troll" : ['Terry', 'Theodore', 'Trall', 'Timb'],
                "Skeleton" : ['DICK', 'HARRY', 'RIBBED', 'Jesus Christ in the Flesh'],
                "Goblin" : ['Harry', 'Balls', 'kekw']
                }

def generate_random_monster():
    global MONSTER_NAME, MONSTER_RACE
    MONSTER_RACE = MONSTER_LIST[random.randint(0, (len(MONSTER_LIST)-1))]
    MONSTER_NAME = MONSTER_NAMES_DICT[MONSTER_RACE][random.randint(0, int(len(MONSTER_NAMES_DICT[MONSTER_RACE])-1))]
    return MONSTER_RACE, MONSTER_NAME

generate_random_monster()

class Monster:
    def __init__(self, hit_points = None, armor = None, attack = None, speed = None, name=MONSTER_NAME, race=MONSTER_RACE):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.name = name
        self.race = race
        if race == 'Goblin':
            self.hit_points = 17
            self.armor = 10
            self.attack = 3
            self.speed = 10
            self.name = name
            self.race = race
        elif race == 'Skeleton':
            self.hit_points = 14
            self.armor = 3
            self.attack = 2
            self.speed = 1
            self.name = name
            self.race = race
        elif race == 'Troll':
            self.hit_points = 13
            self.armor = 6
            self.attack = 6
            self.speed = 8
            self.name = name
            self.race = race

    def __str__(self):
        return str(self.name)

    def __call__(self, *args, **kwargs):
        return self

monster = Monster()
print(monster.name, monster.race, monster.hit_points)
def generate_new_monster():
    global monster
    monster_race = MONSTER_LIST[random.randint(0, (len(MONSTER_LIST)-1))]
    monster_name = MONSTER_NAMES_DICT[monster_race][random.randint(0, int(len(MONSTER_NAMES_DICT[monster_race])-1))]
    monster = Monster(name=monster_name, race=monster_race)
    return monster

generate_new_monster()
print(monster.name, monster.race, monster.hit_points)