# TODO Define classes, and stats.
# TODO Create enemy stats
# TODO Combat actions, attack, run, use item
# TODO Develop inventory, likely using dict
# TODO Exploration Actions

import classes
from classes import combat

Frank = classes.Fighter(name='Frank')

Skeleton = classes.Skeleton(name='Skeletron')
Troll = classes.Troll(name='Terry')

combat(Frank, Troll)
