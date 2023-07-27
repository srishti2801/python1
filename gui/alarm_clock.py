import time

def get_user_input():
    """Get user input for the alarm time."""
    while True:
        try:
            hours = int(input("Enter the hour (0-23): "))
            minutes = int(input("Enter the minutes (0-59): "))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return hours, minutes
            else:
                print("Invalid input. Please enter valid hour (0-23) and minutes (0-59).")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def set_alarm(alarm_hour, alarm_minute):
    """Set the alarm and wait until the specified time is reached."""
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Time's up! Wake up!")
            break

        # Sleep for a short duration (5 seconds) to avoid excessive CPU usage.
        time.sleep(5)

def main():
    print("Welcome to the Python Alarm Clock!")
    print("Please enter the time for the alarm:")
    alarm_hour, alarm_minute = get_user_input()
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

    set_alarm(alarm_hour, alarm_minute)

if __name__ == "__main__":
    main()
