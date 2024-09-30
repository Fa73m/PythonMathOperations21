# Part 2: Alarm Clock Program

# Get the current time from the user
current_time = int(input("Enter the current time (in hours, 24-hour format): "))

# Get the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24

# Display the alarm time
print(f"The alarm will go off at: {alarm_time}:00 hours.")
