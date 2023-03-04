import random

# Player Classes
class PlayerClass:
    def __init__(self, hit_points, armor, attack, speed, name):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.inventory = {}
        self.name = name


    def __str__(self):
        return str(self.name)

    def attack_enemy(self, target):
        if random.randint(0,20) + (self.attack/10) > target.armor:
            damage = random.randint(1, 6)
            target.hit_points -= damage
            return f"You hit {target.name} for {damage}!"
        else:
            return f"Unfortunately you missed {target.name}, try again!"

    def run_from_combat(self, target):
        run_roll = random.randint(1, 20) + (self.speed/10)
        if run_roll > target.speed:
            pass

class Fighter(PlayerClass):
    def __init__(self, hit_points=20, armor=14, attack = 14, speed=10, name=''):
        super().__init__(hit_points, armor, attack, speed, name)


class Rogue(PlayerClass):
    def __init__(self, hit_points=13, armor=20, attack = 14, speed=15, name=''):
        super().__init__(hit_points, armor, attack, speed, name)

class Wizard(PlayerClass):
    def __init__(self, hit_points=13, armor=13, attack = 16, speed=13, name=''):
        super().__init__(hit_points, armor, attack, speed, name)

class Ranger(PlayerClass):
    def __init__(self, hit_points=13, armor=22, attack = 13, speed=16, name=''):
        super().__init__(hit_points, armor, attack, speed, name)

# Monsters

class Monster:
    def __init__(self,  hit_points, armor, attack, speed, name):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack
        self.speed = speed
        self.name = name

    def __str__(self):
        return str(self.name)

    def attack_player(self, target):
        if self.attack > target.armor:
            damage = random.randint(1, 3)
            target.hit_points -= damage

class Goblin(Monster):
    def __init__(self, hit_points=5, armor=8, attack=4, speed=8, name=''):
        super().__init__(hit_points, armor, attack, speed, name)


class Skeleton(Monster):
    def __init__(self, hit_points=8, armor=5, attack=4, speed=2, name=''):
        super().__init__(hit_points, armor, attack, speed, name)

class Troll(Monster):
    def __init__(self, hit_points=14, armor=12, attack=7, speed=6, name=""):
        super().__init__(hit_points, armor, attack, speed, name)



def attack_enemy(self, target):
    if random.randint(0,20) + (self.attack/10) > target.armor:
        damage = random.randint(1, 6)
        target.hit_points -= damage
        return f"You hit {target.name} for {damage}!"
    else:
        return f"Unfortunately you missed {target.name}, try again!"

def combat(player_a, monster_a):
    while monster_a.hit_points > 0 or player_a.hit_points > 0:
        player_choice = input('What would you like to do? \n'
                              'Attack, or run?\n').lower()

        if player_choice == 'attack':
           print(attack_enemy(player_a, monster_a))
           print(attack_enemy(monster_a, player_a))
           if monster_a.hit_points > 0:
               continue
           else:
               print(f"You defeated {monster_a.name}")
               print(monster_a.hit_points)
               break
        elif player_choice == 'run':
            run_chance = (random.randint(0, 20) + player_a.speed)
            if run_chance > monster_a.speed:
                print("You successfully escaped!")
                break
            else:
                 print(attack_enemy(monster_a, player_a))








