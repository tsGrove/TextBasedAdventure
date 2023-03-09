from classes import *

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
        self.attribute = Fighter.attack =+ 1
        self.description = 'A fairly sharp blade, increasing the Fighter\'s attack by one.'
        self.buy = 20
        self.sell = 10

