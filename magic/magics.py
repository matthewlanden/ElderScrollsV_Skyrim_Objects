
class Magic:

    def __init__(self, name, damage, cost):
        self.magic.name = name
        self.magic.damage = damage
        self.magic.cost = cost

    def is_enchanted(self):
        if self.magic.name:
            return True
        return False

class Fire(Magic):
    def __init__(self, name, damage, cost):
        super().__init__(name, damage, cost)

class Frost():
    def __init__(self, name, damage, cost):
        super().__init__(name, damage, cost)
        
class Shock():
    def __init__(self, name, damage, cost):
        super().__init__(name, damage, cost)
