# Task 3: Number Guessing Game
# Generates a random number and tracks the player's attempts with higher/lower hints.

import random

def play_round():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\n--- New Round ---")
    print("I've picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    print("=== Number Guessing Game ===")
    while True:
        play_round()
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
