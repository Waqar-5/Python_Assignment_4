import time

# Function to print with delay for effect (but faster)
def slow_print(text, delay=0.02):  # Reduced delay
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Welcome message
slow_print("\n✨ Welcome to The Mysterious Adventure Mad Libs Game ✨\n", 0.05)

# Get user inputs with clear instructions
name = input("Enter your name here: ").capitalize()
object = input("Enter any object here: ")
place = input("Enter your favorite place here: ")
color = input("Enter your favorite color here: ")
animal = input("Enter your favorite animal here: ")
funny_phrase = input("Enter a funny phrase here: ")
huge_object = input("Enter a huge object here: ")
action_verb = input("Enter an action verb here: ")
adjective = input("Enter an adjective here: ")
creature_of_person = input("Enter a creature or person here: ")
random_dialogue = input("Enter a random dialogue here: ")
past_tense_verb = input("Enter a past tense action here: ")

# Beautifully formatted story output
slow_print(f"\n--- The Great Adventure of {name} ---\n", 0.05)

slow_print(f"\n🌟 One day, {name} decided to explore {place}. With a {object} in hand, they set off on their journey.", 0.05)
slow_print(f"\nSuddenly, a {color} {animal} appeared and blocked the path.", 0.05)

slow_print(f'\n"{funny_phrase}," it said.', 0.05)

slow_print(f"\nConfused but determined, {name} climbed a {object} and discovered a {huge_object} ahead.", 0.05)
slow_print(f"Gathering courage, they decided to {action_verb}.", 0.05)

slow_print(f"\nOut of nowhere, a {adjective} {creature_of_person} appeared and shouted, '{random_dialogue}!',", 0.05)

slow_print(f"\nIn the end, {name} {past_tense_verb} and the adventure ended {adjective}.", 0.05)

# A fun closing message
slow_print("\n🎉 Thanks for playing! 🌟 Hope you enjoyed the adventure! 🎉\n", 0.05)
