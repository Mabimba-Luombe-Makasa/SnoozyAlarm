import time
import datetime
from playsound import playsound


# Function that performs countdown
def countdown_timer():
    try:
        # Gets users preferred time
        user_minutes = int(input("Enter how many minutes in the countdown: "))
        user_seconds = int(input("Enter how many seconds in the countdown: "))
        print("\n")

        # converts minutes to seconds
        total_seconds = user_minutes * 60 + user_seconds

        # For loop gives the number of time remaining in minutes and seconds
        for time_passed in range(total_seconds, 0, -1):
            minutes_remaining = time_passed // 60
            seconds_remaining = time_passed % 60

            # Prints time remaining
            print(f"The time remaining is (MM:SS): {minutes_remaining:02d}:{seconds_remaining:02d}")
            time.sleep(1)

        # Prints this message when the timer is done and plays sound
        print("\nYOUR TIME IS UP\n")
        playsound("alarm.wav")

    # Error handling if user enters a non-numerical character
    except ValueError:
        print("Please enter numerical characters.")


# Function that sets an alarm
def alarm_clock():
    try:
        # Gets user preferred time to set alarm
        user_hours = int(input("Please enter the hour you want to set the alarm: "))
        user_minutes = int(input("Please enter the minutes you want to set the alarm: "))

        # Sets user time into time format
        alarm_time = datetime.time(user_hours, user_minutes)

        # Loop Runs until the time when alarm reaches
        while True:
            current_time = datetime.datetime.now().time()

            # When it is timme it will display message and play sound
            if alarm_time.hour == current_time.hour and alarm_time.minute == current_time.minute:
                print("\nALARM IS RINGING\n")
                playsound("alarm.wav")
                break

            time.sleep(1)
    # Error handling if user enters a non-numerical character
    except ValueError:
        print("Please enter numerical characters for hour and minutes.")


# This function checks the current time
def check_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\nThe TIME is {current_time}\n")


# Title and sub heading
print("SNOOZY ALARM")
print("Always gets you on time...\n")

# While loop will run giving users options
while True:
    # Collects the user option and displays message of options
    user_option = input("Type COUNTDOWN to use Countdown Timer\nType ALARM to use Alarm Clock\n"
                        "Type CLOCK to check current Time\nType EXIT to close the app.\n")
    user_option = user_option.lower()

    if user_option == 'countdown':
        countdown_timer()

    elif user_option == 'alarm':
        alarm_clock()

    elif user_option == 'clock':
        check_time()

    # If user enters EXIT the program will close and print message
    elif user_option == 'exit':
        print("\nThank You for using SNOOZY ALARM")
        break

    # Error handling if user doesn't select the right option
    else:
        print("Please enter a valid option. Try again.")
