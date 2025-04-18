# # Project 6: Countdown Timer Python Project
import time

print("\n ⏲️⏰⏱️ Welcome to the Countdown Timer. ⏲️⏰⏱️ \n")

def countdown_timer(seconds):
    while seconds:
        mins,secs = divmod(seconds, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {time_display} ⏳", end="")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up! ⏰")
try:
    total_time = int(input("Enter the time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("❌Invalid input. Please enter a valid number.")

countdown_timer()
            









# or 


# import time


# def countdown_timer():
#     seconds = 0

#     while True:
#         try:
#             user_input = int(input("Enter the time in seconds: "))
#             if user_input < 0:
#                 print("Please enter a positive number.")
#                 continue
#             seconds += user_input
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue


#     for i in range(seconds, 0, -1):
#         print(f"Time left: {i} seconds", end="\r")
#         time.sleep(1)
#     print("Time's up!")

# countdown_timer()