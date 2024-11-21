import random

class ItemType:
    def __init__(self, name, type, value, rarity="Common"):
        self.name = name
        self.type = type
        self.value = value
        self.rarity = rarity


# Starter Items
COPPER_SWORD = ItemType("Copper Sword", "WEAPON", 5)
STEEL_SWORD = ItemType("Steel Sword", "WEAPON", 12)
IRON_SPEAR = ItemType("Iron Spear", "WEAPON", 8)
SMALL_POTION = ItemType("Small Potion", "POTION", 20)
POTION = ItemType("Potion", "POTION", 40)
LARGE_POTION = ItemType("Large Potion", "POTION", 60)

# Pool of items to grab from
WEAPON_POOL = [COPPER_SWORD, IRON_SPEAR, STEEL_SWORD]
POTION_POOL = [SMALL_POTION, POTION, LARGE_POTION]

class Item:
    def __init__(self, type):
        self.type = type
        self.name = type.name
        self.value = type.value
        self.item_type = type.type

    # Use item method
    def use_item(self, player):
        if self.item_type == "POTION":
            player.heal(self.value)
            return True
        elif self.item_type == "WEAPON":
            player.equipped_weapon = self
            return False
        
    def __str__(self):
        if self.item_type == "WEAPON":
            return f"{self.name} (DMG +{self.value})"
        else:
            return f"{self.name} (Heals {self.value} HP)"