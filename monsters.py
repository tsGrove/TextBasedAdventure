class Monster:
    def __init__(self, name='', race='', attack=0, hit_points=0, speed=0, max_hit_points=0, exp_yield=0, intro=''):
        self.name = name
        self.race = race
        self.attack = attack
        self.hit_points = hit_points
        self.speed = speed
        self.max_hit_points = max_hit_points
        self.exp_yield = exp_yield
        self.intro = intro

    def reset_hit_points(self):
        return self.hit_points == self.max_hit_points

    def __str__(self):
        return str(self.name)

    def __call__(self, *args, **kwargs):
        return self


# Easy Difficulty Monsters ----------------------------------------------------
class Goblin(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Goblin'
        self.attack = 2
        self.armor = 8
        self.hit_points = 8
        self.speed = 12
        self.max_hit_points = 8
        self.exp_yield = 2
        self.bloodied = 'The Goblin barely grasping at his crossbow, readies to take one final shot.'
        self.intro = 'You see a small green creature moving in the shadows, a goblin appears!'


class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Skeleton'
        self.attack = 1
        self.armor = 6
        self.hit_points = 6
        self.speed = 5
        self.max_hit_points = 6
        self.exp_yield = 3
        self.bloodied = 'The skeleton, mostly fallen apart, raises its only arm in an attempt to strike back.'
        self.intro = 'A mound of bones jumps to life, a skeleton charges towards you!'


class Kobold(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Kobold'
        self.attack = 3
        self.armor = 4
        self.hit_points = 5
        self.max_hit_points = 5
        self.exp_yield = 2
        self.bloodied = 'Letting out a vicious snarl, the Kobold desperately lunges at you with a dagger!'
        self.intro = 'Is that a baby dragon!?! Oh thank god, its just a Kobold, but its coming right at you!'


# Medium Difficulty Monsters ----------------------------------------------------------------------------------------
class Troll(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Troll'
        self.attack = 7
        self.armor = 7
        self.hit_points = 13
        self.speed = 10
        self.max_hit_points = 13
        self.exp_yield = 5
        self.bloodied = 'Its regeneration not enough to withstand your attacks, the Troll lets out a cry and thrashes its club about!'
        self.intro = 'A mighty troll blocks the door before you, raising its club, get down!'


class Ghoul(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Ghoul'
        self.attack = 8
        self.armor = 8
        self.hit_points = 10
        self.max_hit_points = 10
        self.exp_yield = 7
        self.bloodied = 'The ghoul, missing parts and pieces, attempts to claw your brains out!'
        self.intro = 'Razor-sharp teeth and jagged claws, a pale ghoul emerges from the shadows!'


class Ooze(Monster):
    def __int__(self):
        super().__init__()
        self.race = 'Ooze'
        self.armor = 4
        self.hit_points = 16
        self.max_hit_points = 16
        self.exp_yield = 8
        self.bloodied = 'Giant green piles of ooze cover the ground as you cleave through it, the cube looks like its falling apart!'
        self.intro = 'This room looks strangely....clean? Something green drips down from the ceiling...its  Gelatinous Cube!'


# Hard Difficulty Monsters ---------------------------------------------------------------------------------------
class ClayGolem(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Clay Golem'
        self.armor = 15
        self.hit_points = 20
        self.max_hit_points = 20
        self.exp_yield = 13
        self.bloodied = 'Bits of dust and clay cover the ground, as the Golem raises its arms in an attempt to pancake you!'
        self.intro = 'You hear a rhythmic shaking, the ground moving beneath your feet. A Clay Golem appears before you!'


class BoneDevil(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Bone Devil'
        self.armor = 17
        self.hit_points = 17
        self.max_hit_points = 17
        self.exp_yield = 12
        self.bloodied = 'Fragments of bone and dust covering the ground before you, the Bone Devil raises its stinger ready to pierce you.'
        self.intro = 'A large white creature with a blood drenched stinger-like tail comes crawling out of the dark, its a Bone Devil!'


class YoungBlackDragon(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Young Black Dragon'
        self.armor = 20
        self.hit_points = 23
        self.max_hit_points = 23
        self.exp_yield = 15
        self.bloodied = 'As blood drips from the dragons maw, you see its mouth close and green gas start to leak as its attempts to poison you!'
        self.intro = 'This room smells of...poison, your nostrils burn. In the distance you see a...pile of treasure? Sitting atop is it Young Black Dragon!'


# Boss Monsters -----------------------------------------------------------------------------------------------------
class Vampire(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Vampire'
        self.armor = 23
        self.hit_points = 30
        self.max_hit_points = 30
        self.exp_yield = 20
        self.bloodied = 'The vampire smiles, bearing its blood-coated fangs as it gives you a moment of reprieve, before lunging from the shadows.'
        self.intro = 'A long black cloak and white fangs adorned with a confident smile, ready your stakes, its a Vampire!'

class Lich(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Lich'
        self.armor = 20
        self.hit_points = 34
        self.max_hit_points = 34
        self.exp_yield = 20
        self.bloodied = 'Raising its staff, you feel the temperature in the air drop around you, the room becomes cold and the air dense.'
        self.intro = 'Floating above the ground, wielding a staff emitting great power, a Lich appears to defend its phylactery!'

class AdultBlackDragon(Monster):
    def __init__(self):
        super().__init__()
        self.race = 'Adult Black Dragon'
        self.armor = 25
        self.hit_points = 33
        self.max_hit_points = 33
        self.exp_yield = 20
        self.bloodied = 'Blood and poison running down the mouth of the dragon, you see it rear back as it attempts to devour you!'
        self.intro = 'The biggest treasure hoard you\'ve ever seen sits in front of you, but to get through it you need to defeat the Adult Black Dragon!'

# Monster Names --------------------------------------------------------------------------------------------------
MONSTER_NAMES_DICT = {
                "Troll" : ['Stinky Steve', 'Fart Breath Harold', 'Pam’kol', 'Shexoha'],
                "Skeleton" : ['Bones McCoy', 'Indiana Bones', 'Jerry Spinefeld', 'Bona Lisa', 'Skelly Clarkson'],
                "Goblin" : ['Bankrup', 'Clird', 'Shake Spear', 'Silverpants', 'Pantoran'],
                "Kobold" : ['Meepo', 'Scruntbuff', 'Quesarito', 'Lemmiewinks', 'Gitimahorse']
                }

# Monsters Dictionary --------------------------------------------------------------------------------------------
EASY_MONSTERS_DICT = {
                'Goblin' : Goblin(),
                'Kobold' : Kobold(),
                'Skeleton' : Skeleton()
                    }

MEDIUM_MONSTERS_DICT = {
                    'Troll' : Troll(),
                    'Ghoul' : Ghoul(),
                    'Ooze' : Ooze(),
                    }

HARD_MONSTER_DICT = {
                    'Clay Golem' : ClayGolem(),
                    'Bone Devil' : BoneDevil(),
                    'Young Black Dragon' : YoungBlackDragon(),
}

BOSS_MONSTERS_DICT = {
                    'Vampire' : Vampire(),
                    'Lich' : Lich(),
                    'Adult Black Dragon' : AdultBlackDragon()
}

# Monsters by List -----------------------------------------------------------------------------------------------
EASY_MONSTER_LIST = ['Goblin', 'Skeleton', 'Kobold']
MEDIUM_MONSTER_LIST = ['Troll', 'Ghoul', 'Ooze']
HARD_MONSTER_LIST = ['Clay Golem', 'Bone Devil', 'Young Black Dragon']
BOSS_MONSTER_LIST = ['Vampire', 'Lich', 'Adult Black Dragon']
