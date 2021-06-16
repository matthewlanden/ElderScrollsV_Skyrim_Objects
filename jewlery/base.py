from base.base_item import Item

class Jewelery(Item):
    def __init__(self, name: str, weigh: float, price: int):
        super().__init__(name, weigh, price)
