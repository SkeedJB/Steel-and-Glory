from classes.player import Player
from classes.enemy import Enemy
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

if __name__ == "__main__":
    test_enemy()



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