from base.base_levels import Level
from base.base_item import Item


class Weapon(Item, Level):
    
    def __init__(self, name: str, weigh: float, price: int, level:int, damage:int):
        
        Item.__init__(self, name, weigh, price)
        Level.__init__(self, level)
        self.damage = damage

    def __str__(self):
        return self.name

    def deal_damage(self):
        print(f'enemy has lost {self.damage * 11} HP')
       