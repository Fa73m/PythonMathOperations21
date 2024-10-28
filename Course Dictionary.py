# Define dictionaries for room numbers, instructors, and meeting times
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Loop to allow multiple searches
while True:
    # Prompt user for a course number
    course_number = input("Enter a course number (e.g., CSC101) or 'q' to quit: ")
    
    # Check if the user wants to quit
    if course_number.lower() == 'q':
        print("Exiting program. Goodbye!")
        break

    # Check if the course exists and display details
    if course_number in room_numbers:
        room = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Course not found. Please try again.")
