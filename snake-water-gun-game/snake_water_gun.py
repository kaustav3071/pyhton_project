import random

def exit_game():
    """Exits the game with a thank-you message."""
    print("Exiting the GAME.")
    print("***THANK YOU***")


print("""
**** WELCOME TO THE SNAKE WATER GUN GAME ****
1. ENTER THE GAME
2. EXIT FROM THE GAME
""")

choice = int(input("ENTER YOUR CHOICE: "))

if choice == 1:
    print("\n** IF YOU WANT TO EXIT DURING THE GAME, PRESS 0 **")
    options = ["SNAKE", "WATER", "GUN"]
    
    while True:
        print("\n--- NEW ROUND ---")
        
        
        user1 = random.choice(options)
        print("Computer has made its choice.\n")
        
       
        user2 = input("User 2, Enter your guess (SNAKE/WATER/GUN): ").upper()
        print()
        
        
        print(f"COMPUTER'S CHOICE: {user1}")
        print(f"YOUR CHOICE: {user2}")
        print()
        
        
        if user2 == "0":
            exit_game()
            break
        
        
        if user2 not in options:
            print("INVALID INPUT! Please choose SNAKE, WATER, or GUN.")
            continue
        
        
        if user1 == "GUN" and user2 == "SNAKE":
            print("Computer wins with GUN!")
        elif user2 == "GUN" and user1 == "SNAKE":
            print("You win with GUN!")
        elif user2 == "WATER" and user1 == "SNAKE":
            print("Computer wins with SNAKE!")
        elif user1 == "WATER" and user2 == "SNAKE":
            print("You win with SNAKE!")
        elif user2 == "GUN" and user1 == "WATER":
            print("Computer wins with WATER!")
        elif user1 == "GUN" and user2 == "WATER":
            print("You win with WATER!")
        elif user1 == user2:
            print("... IT'S A DRAW ...")
        
elif choice == 2:
    exit_game()
else:
    print("INVALID CHOICE! Please enter 1 to play or 2 to exit.")
