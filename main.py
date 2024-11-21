from classes.player import Player
from classes.enemy import Enemy
from classes.item import Item, WEAPON_POOL, POTION_POOL, ItemType
from utils.game_data import save_game, load_game, delete_save
import random

def main():
    while True: 
        print("""
        =====================================
        =     WELCOME TO STEEL AND GLORY    =
        =====================================""")
        print("1. New Game")
        print("2. Load Game")
        print("3. Delete Save")
        print("4. Quit")

        choice = input("Enter your choice:")
        if choice == "1":
            print("Starting new game...")
            player_name = input("Enter your character's name: ")
            player = Player(player_name)
            # Gives starting items
            # Gives player random starting items
            player.add_item(Item(random.choice(WEAPON_POOL)))
            player.add_item(Item(random.choice(POTION_POOL)))
            game_loop(player)
        elif choice == "2":
            player = load_game()
            if player is not None:
                game_loop(player)
        elif choice == "3":
            delete_save()
        elif choice == "4":
            print("See you soon.")
            return
        else:
            print("Invalid choice!")

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
        print("│ 2. Item     │")
        print("│ 3. Check Inv│")
        print("└─────────────┘")
        choice = input("Enter your choice:")

        # Attack functions
        if choice == "1":
            
            print("\n" + ">"*20 + " ATTACK! " + "<"*20)
            
            # Player turn
            player_damage = player.attack()
            print(f"⚔️You attack and deal {player_damage:.2f} damage!⚔️")
            enemy_alive = enemy.take_damage(player_damage)

            # Enemy turn if alive
            if enemy_alive:
                enemy_damage = enemy.attack()
                print(f"{enemy.name} strikes for {enemy_damage:.2f} damage!")
                player.take_damage(enemy_damage)


        # Item use functions
        elif choice == "2":

            print("\n" + ">"*20 + " ITEM! " + "<"*20)
            player.show_inventory()
            if len(player.inventory) > 0:
                item_choice = int(input("Choose item number: (0 to cancel)")) - 1
                if item_choice >= -1:
                    if item_choice == -1:
                        print("Canceled item use.")
                    else:
                        item = player.inventory[item_choice]
                if item.item_type == "POTION":
                    print(f"\n❤️ You heal for {item.value} HP!")
                elif item.item_type == "WEAPON":
                    print(f"\n⚔️ You equip the {item.name}!")
                player.use_item(item_choice)

            # Enemy attack after item use
                enemy_damage = enemy.attack()
                print(f"⚔️ {enemy.name} attacks you for {enemy_damage:.2f} damage!⚔️")
                player.take_damage(enemy_damage)

        elif choice == "3":
            player.show_inventory()
            input("Press Enter to continue...")

        else:
            print("Invalid choice. Turn Lost")

        # Combat results 
    if player.is_alive():
        print("\n" + "*"*40)
        print(f"You defeated the {enemy.name}! 🏆")
        print("*"*40)
        # Gain exp
        exp_gained = enemy.get_exp_gain()
        player.gain_exp(exp_gained)
        print(f"You gained {exp_gained} EXP!")
        # Get loot: 50% chance of loot drop, then 50% chance if weapon or potion
        if random.random() < 0.5:
            if random.random() < 0.5:
                dropped_item = Item(random.choice(WEAPON_POOL))
            else:
                dropped_item = Item(random.choice(POTION_POOL))
            print(f"You found: {dropped_item}")
            player.add_item(dropped_item)
        return True
    else:
        print("\n" + "x"*40)
        print("💀 You were defeated... 💀")
        print("x"*40)
        return False


    # Main game loop
def game_loop(player):

    # Game loop
    while player.is_alive():
        
        # Generate enemy
        enemy = Enemy.generate_enemy(player.level)
        
        # Start combat
        combat_result = simple_combat(player, enemy)
        
        if not combat_result:
            break
        
        # Ask to continue, save, or quit
        print("\n1. Continue fighting")
        print("2. Save and return to menu")
        print("3. Quit without saving")
        choice = input("Choose an option: ")
        
        if choice == "1":
            continue
        elif choice == "2":
            save_game(player)
            return
        else:
            break
    
    print("Game Over!")

if __name__ == "__main__":
    main()