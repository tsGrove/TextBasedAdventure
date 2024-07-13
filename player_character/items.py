class Item:
    def __init__(self, name='', attribute='', buy_value=0, sell_value=0, description=''):
        self.name = name
        self.attribute = attribute
        self.buy = buy_value
        self.sell = sell_value
        self.description = description

    def __call__(self, *args, **kwargs):
        return self


class Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Blade of Monster Hurting'
        self.description = 'a fairly sharp blade, increasing your attack by one'
        self.buy = 20
        self.sell = 10


class Armor(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Superior Armor'
        self.description = 'a set of sturdy leather armor, making you more resilient against monster attacks'
        self.buy = 20
        self.sell = 8


class Boots(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Boots of Swiftness'
        self.description = 'a pair of boots increasing your speed, making it more likely for you to dodge traps, and attack before monsters'
        self.buy = 13
        self.sell = 6


class HealthPotion(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Potion of Healing'
        self.description = 'A bright red beverage, slightly bubbling in a crystal vial. Smells of cherry, restores HP to full, single use'
        self.buy = 50
        self.sell = 10


    def drink_potion(self):
        self.attribute = player_character.health_points = player_character.max_hit_points