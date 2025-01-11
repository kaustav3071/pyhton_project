import random

def play_guessing_game():
    comp = random.randint(1, 5)
    player = -1

    print("🎮 Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 5. Can you guess it?")

    while comp != player:
        try:
            player = int(input("Enter your guess (1-5): "))

            if player < 1 or player > 5:
                print("🚫 Please guess a number within the range 1-5.")
                continue

            if player > comp:
                print("📈 Too high!")
            elif player < comp:
                print("📉 Too low!")
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

    print("🎉 Congratulations! You guessed the correct number.")

if __name__ == "__main__":
    play_guessing_game()
