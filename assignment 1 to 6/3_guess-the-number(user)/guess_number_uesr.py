import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def user_guess_game():
    print("\n🎮 Welcome to the Ultimate Number Guessing Challenge! 🔢✨\n")
    print("Choose your difficulty level:")
    print("🟢 Easy (1-10)")
    print("🟡 Medium (1-50)")
    print("🔴 Hard (1-100)")

    level = input("\n🎯 Enter difficulty (easy/medium/hard): ").lower()
    
    if level == "easy":
        max_num = 10
    elif level == "medium":
        max_num = 50
    elif level == "hard":
        max_num = 100
    else:
        print("⚠️ Invalid choice. Defaulting to Easy.")
        max_num = 10

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\n🤖 I'm thinking of a number between 1 and {max_num}. Try to guess it!\n")

    while True:
        try:
            guess = int(input("🔢 Your guess: "))
            attempts += 1

            if guess < 1 or guess > max_num:
                print(f"⚠️ Please guess a number between 1 and {max_num}.")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                slow_print(f"\n🎉 Correct! You guessed the number {secret_number} in {attempts} attempts! 🥳")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# 🔁 Loop to replay the game
while True:
    user_guess_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for playing! Come back soon.")
        break
