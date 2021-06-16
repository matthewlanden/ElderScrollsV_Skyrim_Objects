from base.base_levels import Level





class  Enchant:

    def __init__(self, enchant, level:Level):
        self.enchant = enchant
        self.enchant.level = level