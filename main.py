from classes.player import Player
from classes.enemy import Enemy
import random

def main(): 
    print("""
    =====================================
    =     WELCOME TO STEEL AND GLORY    =
    =====================================""")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Enter your choice:")
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

# Basic combat loop
def simple_combat(player, enemy):
    print(f"As the iron door opens, a fierce {enemy.name} comes into the ring.")
    print("\n" + "="*40)
    print(f"⚔️  BATTLE START: {player.name} vs {enemy.name}  ⚔️")
    print("="*40)

    while player.is_alive() and enemy.is_alive():
        # Displays player stats and enemy stats
        print("\n" + str(player))
        print(str(enemy))

        # Player Turn
        print("\n" + "─"*40)
        print("Your turn:")
        print("┌─────────────┐")
        print("│ 1. Attack   │")
        print("│ 2. Heal     │")
        print("└─────────────┘")
        choice = input("Enter your choice:")

        # Attack functions
        if choice == "1":
            
            print("\n" + ">"*20 + " ATTACK! " + "<"*20)
            
            # Player turn
            player_damage = player.attack()
            print(f"You attack and deal {player_damage:.2f} damage!")
            enemy_alive = enemy.take_damage(player_damage)

            # Enemy turn if alive
            if enemy_alive:
                enemy_damage = enemy.attack()
                print(f"{enemy.name} strikes for {enemy_damage:.2f} damage!")
                player.take_damage(enemy_damage)


        # Heal functions
        elif choice == "2":

            print("\n" + ">"*20 + " HEAL! " + "<"*20)

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
        print("\n" + "*"*40)
        print(f"You defeated the {enemy.name}! 🏆")
        print("*"*40)
        # Gain exp
        exp_gained = enemy.get_exp_gain()
        player.gain_exp(exp_gained)
        print(f"You gained {exp_gained} EXP!")
        # Get loot
        loot = enemy.drop_loot()
        print(f"You found: {loot}")
        return True
    else:
        print("\n" + "x"*40)
        print("💀 You were defeated... 💀")
        print("x"*40)
        return False


# Main game loop
def main():
    # Create player
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    
    # Game loop
    while player.is_alive():
        
        # Generate enemy
        enemy = Enemy.generate_enemy(player.level)
        
        # Start combat
        combat_result = simple_combat(player, enemy)
        
        if not combat_result:
            break
        
        # Ask to continue
        continue_game = input("Continue fighting? (y/n): ")
        if continue_game.lower() != 'y':
            break
    
    print("Game Over!")

if __name__ == "__main__":
    main()