import random

# 🎨 Hangman stages (from full to empty)
hangman_stages = [
    """
     _______
    |/      |
    |      😵
    |      /|\\
    |      / \\
    |
    |___
    """,
    """
     _______
    |/      |
    |      😧
    |      /|\\
    |      /
    |
    |___
    """,
    """
     _______
    |/      |
    |      😥
    |      /|\\
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      😐
    |      /|
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      😬
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      🙂
    |
    |
    |
    |___
    """,
    """
     _______
    |/      
    |
    |
    |
    |
    |___
    """
]

# 🎯 Word bank
word_list = ["python", "hangman", "challenge", "programming", "adventure"]

# 🧠 Pick a random word
chosen_word = random.choice(word_list)
word_display = ["_"] * len(chosen_word)
guessed_letters = []
lives = 6

print("\n🪢 Welcome to the Advanced Hangman Game! 🪢")
print("🧩 Your word has", len(chosen_word), "letters.")
print(" ".join(word_display))

# 🎮 Game loop
while lives > 0 and "_" in word_display:
    guess = input("\n🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good job! The letter is in the word.")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        lives -= 1
        print(f"❌ Wrong guess! You have {lives} {'life' if lives == 1 else 'lives'} left.")
        print(hangman_stages[6 - lives])

    print("\n🧩 Word: " + " ".join(word_display))
    print("📜 Guessed letters:", ", ".join(guessed_letters))

# 🏁 End of game
if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 You ran out of lives. The word was:", chosen_word)
    print("😢 Better luck next time!")
