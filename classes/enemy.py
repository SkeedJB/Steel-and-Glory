import random

# Creates variable enemy types
class EnemyType:
    def __init__(self, strength_multiplier, hp_multiplier, exp_gain):
        self.strength_multiplier = strength_multiplier
        self.hp_multiplier = hp_multiplier
        self.exp_gain = exp_gain

        # Predefined enemy types
GOBLIN = EnemyType(strength_multiplier=15, hp_multiplier=30, exp_gain=20)
DRAGON = EnemyType(strength_multiplier=80, hp_multiplier=150, exp_gain=250)
ORC = EnemyType(strength_multiplier=20, hp_multiplier=50, exp_gain=40)
TROLL = EnemyType(strength_multiplier=23, hp_multiplier=80, exp_gain=60)
OGRE = EnemyType(strength_multiplier=30, hp_multiplier=100, exp_gain=80)
DEMON = EnemyType(strength_multiplier=100, hp_multiplier=200, exp_gain=300)

ENEMY_POOLS = {
            "early": [GOBLIN, ORC],
            "mid": [TROLL, OGRE],
            "late": [DRAGON, DEMON]
        }

# Enemies will inherit from this class to form different types.
class Enemy:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.exp_gain = type.exp_gain * self.level

        # Decides how strong the enemy will be based on the multi 
        self.strength_multiplier = type.strength_multiplier
        self.strength = (self.level * self.strength_multiplier)

        # Decides how much hp the enemy has based on its multi
        self.hp_multiplier = type.hp_multiplier
        self.hp = (self.level * self.hp_multiplier)
        self.max_hp = self.hp
        
        # Will hold a list of possible items for the enemy to drop
        self.loot = ["Sword", "Axe", "Dagger"]

    def drop_loot(self):
        return random.choice(self.loot)

    # Reduces hp based on damage amount, 
    # *** Make this based on player's attack damage? ***
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

    # Scale and generate enemies with player level
    def generate_enemy(player_level):
        
        # Enemy will could be between one level lower or 
        # 2 levels higher than player
        enemy_level = player_level + random.randint(-1, 2)
        enemy_level = max(1, enemy_level)
      
        # Chooses prefix based on level difference
        prefixes = ["Weak", "Normal", "Strong", "Legendary"]
        if enemy_level > player_level:
            enemy_prefix = random.choice(prefixes[-2:])
        elif enemy_level == player_level:
            enemy_prefix = prefixes[1]
        else:
            enemy_prefix = prefixes[0]

        if player_level >= 10:
            pool = ENEMY_POOLS["late"]
        elif player_level >= 5:
            pool = ENEMY_POOLS["mid"]
        else:
            pool = ENEMY_POOLS["early"]

        enemy_type = random.choice(pool)

        return Enemy(f"{enemy_prefix} {type(enemy_type).__name__}",
                      enemy_level, enemy_type)

