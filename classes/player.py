import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.strength = 25
        self.exp = 0
        self.inventory = []


    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.strength += 8
        self.hp = self.max_hp
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            return False
        else:
            return True

    def heal(self, amount):
        self.hp += amount
        if self.hp >= self.max_hp:
            pass

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
        damage = self.strength * random.random()
        return damage
    
    def __str__(self):
        return f"""
    {self.name}'s Status:
    Level: {self.level}
    HP: {self.hp}/{self.max_hp}
    Strength: {self.strength}
    EXP: {self.exp}/100
    """
