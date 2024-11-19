from classes.player import Player
from classes.enemy import Enemy
import random

def main(): 
    print("-----------------------------------")
    print("Welcome to Steel and Glory.")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Enter your choice: (1, 2, 3) ")
    if choice == "1":
        print("Starting new game...")
    elif choice == "2":
        print("Loading game...")
    elif choice == "3":
        print("See you soon.")
        return
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

def test_enemy():
    # Create Enemy
    enemy = Enemy("Enemy", 1, 25, 20, 50)
    print("Initial stats:")
    print(enemy)

    # Tests attack
    damage = enemy.attack()
    print(f"Enemy attacks for {damage} damage!")

    # Tests taking damage
    print("\nTaking 30 damage...")
    enemy.take_damage(5)
    print(enemy)


    # On enemy death displays a random item from possible loot and displays exp gained
    print("Killing and dropping loot..")
    enemy.take_damage(50)
    print(enemy.is_alive())
    print(enemy)


def test_player():
    # Create a player
    hero = Player("Hero")
    print("Initial status:")
    print(hero)
    
    # Test attack
    damage = hero.attack()
    print(f"Hero attacks for {damage} damage!")
    
    # Test taking damage
    print("\nTaking 30 damage...")
    hero.take_damage(30)
    print(hero)
    
    # Test healing
    print("Healing 20 HP...")
    hero.heal(20)
    print(hero)
    
    # Test gaining exp and leveling up
    print("Gaining 150 exp...")
    hero.gain_exp(150)  # This should trigger a level up
    print(hero)

# Basic combat loop
def simple_combat(player, enemy):
    print(f"As the iron door opens, a fierce {enemy.name} comes into the ring.")

    while player.is_alive() and enemy.is_alive():
        # Displays player stats and enemy stats
        print("\n" + str(player))
        print(str(enemy))

        # Player Turn
        print("\nYour Move:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter your choice:")

        # Attack functions
        if choice == "1":
            
            # Player turn
            player_damage = player.attack()
            print(f"You attack and deal {player_damage:.2f} damage!")
            enemy_alive = enemy.take_damage(player_damage)

            # Enemy turn if alive
            if enemy_alive:
                enemy_damage = enemy.attack()
                print(f"{enemy.name} attacks you for {enemy_damage:.2f} damage!")
                player.take_damage(enemy_damage)


        # Heal functions
        elif choice == "2":
            heal_amount = random.randint(10,25)
            player.heal(heal_amount)
            print(f"You heal for {heal_amount} HP")

            # Enemy attack after heal
            enemy_damage = enemy.attack()
            print(f"{enemy.name} attacks you for {enemy_damage:.2f} damage!")
            player.take_damage(enemy_damage)

        else:
            print("Invalid choice. Turn lost.")

        # Combat results 
    if player.is_alive():
        print(f"You defeated the {enemy.name}!")
        # Gain exp
        exp_gained = enemy.get_exp_gain()
        player.gain_exp(exp_gained)
        print(f"You gained {exp_gained} EXP!")
        # Get loot
        loot = enemy.drop_loot()
        print(f"You found: {loot}")
        return True
    else:
        print("You were defeated...")
        return False
    


# Main game loop
def main():
    # Create player
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    
    # Game loop
    while player.is_alive():
        # Create an enemy
        enemy = Enemy("Goblin", level=1, strength_multiplier=10, exp_gain=50, hp_multiplier=20)
        
        # Start combat
        combat_result = simple_combat(player, enemy)
        
        if not combat_result:
            break
        
        # Ask to continue
        continue_game = input("Continue adventuring? (y/n): ")
        if continue_game.lower() != 'y':
            break
    
    print("Game Over!")

if __name__ == "__main__":
    main()