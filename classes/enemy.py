import random

# Enemies will inherit from this class to form different types.
class Enemy:
    def __init__(self, name, level, strength_multiplier, exp_gain, hp_multiplier):
        self.name = name
        self.level = level
        self.exp_gain = exp_gain

        # Decides how strong the enemy will be based on the multi 
        self.strength_multiplier = strength_multiplier
        self.strength = (self.level * self.strength_multiplier)

        # Decides how much hp the enemy has based on its multi
        self.hp_multiplier = hp_multiplier
        self.hp = (self.level * self.hp_multiplier)
        self.max_hp = self.hp
        
        # Will hold a list of possible items for the enemy to drop
        self.loot = ["Sword", "Axe", "Dagger"]

    def drop_loot(self):
        return random.choice(self.loot)

    # Reduces hp based on damage amount, *** Make this based on player's attack damage? ***
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.drop_loot()
        else:
            return True
        
    # Checks if enemy still has hp remaining    
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            print(f"""    
    Items Dropped on Death: {self.drop_loot()}
    EXP Gained: {self.get_exp_gain()}""")
        
    def attack(self):
        multipliers = [0.5, 1.0, 1.2, 1.4, 1.5, 2.0]
        damage = self.strength * (random.choice(multipliers))
        return damage

    def get_exp_gain(self):
        return self.exp_gain * 1

    def __str__(self):
        return f"""
    {self.name}'s Status:
    Level: {self.level}
    HP: {self.hp}/{self.max_hp}
    Strength: {self.strength}
    """

    

