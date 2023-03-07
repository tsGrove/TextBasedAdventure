import random

def attack_enemy(player, target):
    if random.randint(0,20) + (player.attack/10) > target.armor:
        damage = random.randint(1, 6) + player.attack
        target.hit_points -= damage
        return f"You hit {target.name} for {damage}!"
    else:
        return f"Unfortunately you missed {target.name}, try again!"

def combat(player, monster):
    encounter = True
    while encounter:
        print(f"Oh shit, theres {monster}, the {monster.race}!")
        player_choice = input('What would you like to do? \n'
                              'Attack, or run?\n').lower()
        if player_choice == 'attack':
           print(attack_enemy(player, monster))
           print(attack_enemy(monster, player))
           if monster.hit_points > 0 and player.hit_points > 0:
               continue
           elif monster.hit_points <= 0:
               print(f"You defeated {monster.name}")
               encounter = False
           elif player.hit_points <= 0:
               print(f"{monster.name} defeated you! Oh no! Better luck next time")
               encounter = False


        elif player_choice == 'run':
            run_chance = (random.randint(0, 20) + player.speed)
            if run_chance > monster.speed:
                print("You successfully escaped!")
                encounter = False
            else:
                 print(attack_enemy(monster, player))

        else:
            print("Please enter a valid option, either 'Attack', or 'Run'.")