from dataclasses import dataclass

from items.item import Item

@dataclass
class Weapon(Item):
    damage:int 
    #durability:int
    