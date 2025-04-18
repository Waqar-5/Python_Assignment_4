import time
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def computer_guess():
    print("\n🎮 Welcome to the AI Number Guessing Game! 🤖")
    print("🤔 Think of a number between 1 and 100. I, the computer, will try to guess it!\n")
    input("🧠 Press Enter when you're ready...")

    low = 1
    high = 10
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        slow_print(f"🤖 Is your number... {guess}?")

        feedback = input("👉 Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            slow_print(f"\n🎉 Yay! I guessed your number {guess} in {attempts} attempts!\n")
            break
        else:
            print("⚠️ Please enter only 'h', 'l', or 'c'.")

    if low > high:
        print("\n😵 I couldn't guess it. Something went wrong. Let's try again!\n")

# 🔁 Play again loop
while True:
    computer_guess()
    play_again = input("🔁 Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing! See you next time.")
        break
