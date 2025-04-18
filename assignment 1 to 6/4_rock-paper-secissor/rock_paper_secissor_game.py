# 🌟 Advanced Project 4: Rock, Paper, Scissors with Scoreboard
import random
import time


def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def user_choice():
    while True:
        choice = input("\n ✋ Choose 'rock', 'paper', 'scissors': ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("⚠️ Invalid choice, please choose 'rock', 'paper', or 'scissors'.")


def ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, ai):
    if user == ai:
        return "draw"
    elif (user == 'rock' and ai == 'scissors') or \
        (user == 'scissors' and ai == 'paper') or \
        (user == 'paper' and ai == 'rock'):
        return "user"
    else:
        return "ai"
    
def game():
    user_score = 0
    ai_score = 0
    rounds = 0

    
    print("\n🎮 Welcome to Rock, Paper, Scissors! 🪶⚡")

    while True:
        print("\n🏁 Round", rounds + 1)
        user = user_choice()
        ai = ai_choice()

        print(f"\n🤖 AI chose: {ai}")
    
        winner = determine_winner(user, ai)

        if winner == "user":
            user_score += 1
            slow_print(f"\n🎉 You won this round! {user.capitalize()} beats {ai}!")
        elif winner == "ai":
            ai_score += 1
            slow_print(f"\n😞 You lost this round. {ai.capitalize()} beats {user}!")
        else:
            slow_print("\n🤝 It's a draw!")
    
        print(f"\n🏆 Current Score - You: {user_score} | AI: {ai_score}")
        rounds += 1


        play_again = input("\n🔁 Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\n🎉 Final Score - You: {user_score} | AI: {ai_score}")
            print("👋 Thanks for playing! See you next time.")
            break


# 🎮 Run the game
game()


