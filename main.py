from classes.player import Player

def main(): 
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

def test_player():
    # Create a player
    hero = Player("Hero")
    print("Initial status:")
    print(hero)
    
    # Test attack
    damage = hero.attack()
    print(f"Hero attacks for {damage:.2f} damage!")
    
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

if __name__ == "__main__":
    test_player()