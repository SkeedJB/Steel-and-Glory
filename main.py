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