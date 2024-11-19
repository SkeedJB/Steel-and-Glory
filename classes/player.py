import random
from classes.item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.strength = 40
        self.exp = 0
        self.inventory = []
        self.equipped_weapon = None

    # Add item to inventory
    def add_item(self, item):
        self.inventory.append(item)
        if item.item_type == "WEAPON" and self.equipped_weapon is None:
            item.use_item(self)
            print(f"\nEquipped: {item.name}")

    # Equip weapon or consume potion
    def use_item(self, item_index):
        
        # Checks if inventory is empty
        if len(self.inventory) == 0:
            print("Inventory is empty!")
            return

        # Checks if index within inventory bounds
        if item_index >= len(self.inventory) or item_index < 0:
            print("Invalid choice.")
            return
        
        # Get item from inventory
        item = self.inventory[item_index]
        
        # If using item returns true, it is a potion and gets removed
        consumed = item.use_item(self)
        if consumed:
            self.inventory.pop(item_index)

    def show_inventory(self):
        print("\n═══════════ EQUIPMENT ═══════════")
        if self.equipped_weapon is None:
            print("No weapon equipped.")
        else:
            print(f"Equipped: {self.equipped_weapon}")

        print("\n═══════════ INVENTORY ═══════════")
        if len(self.inventory) == 0:
            print("Inventory is empty.")
            return
        
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}: {item}")
            
    def level_up(self):
        self.level += 1
        self.max_hp += 50
        self.strength += 25
        self.hp = self.max_hp
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            return False
        else:
            return True

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level_up()

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
    
    def attack(self):
        base_damage = self.strength
        # Checks if weapon is equipped and returns damage value, else adds 0
        weapon_damage = self.equipped_weapon.value if self.equipped_weapon else 0
        multipliers = [0.5, 1.0, 1.2, 1.4, 1.5, 1.8, 2.0]
        damage = (base_damage + weapon_damage) * (random.choice(multipliers))
        return damage
    
    # Status display
    def __str__(self):
        return f"""
        ┌{'─'*30}┐
        │ {self.name}'s Status:
        │ Level: {self.level}
        │ HP: {self.hp}/{self.max_hp}
        │ Strength: {self.strength}
        │ EXP: {self.exp}
        │ Equipped Weapon: {self.equipped_weapon}
        └{'─'*30}┘
        """   
