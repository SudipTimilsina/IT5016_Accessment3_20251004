
Student Attendance Tracking System

This is a simple Python program that allows a training institute or classroom to track student attendance. It demonstrates basic Object-Oriented Programming (OOP) concepts like classes, objects, and class variables, without using advanced Python features.

Features
Add Students: Add new students interactively with name and attendance percentage.
Automatic ID Assignment: Each student receives a unique ID automatically.
Display Students: View all students with their ID, name, and attendance.
Update Attendance: Modify a student’s attendance by entering their ID.
Average Attendance: Calculate the average attendance for all students.
Handles empty lists gracefully — no students, no errors.
How It Works
All students are stored in a class-level list (allStudents).
Each student object has:
studentName
studentID (auto-incremented)
studentAttendance
Users interact with the system via a menu:
Add Student
Update Student Attendance
Display All Students
Show Average Attendance
Quit
The system continues to run until the user chooses to quit.
Getting Started
Make sure you have Python 3 installed.
Copy the Student class program into a .py file, e.g., attendance_system.py.
Run the program using:
python attendance_system.py
Follow the menu prompts to add, update, or view students.


Example Usage
--- Student Attendance System ---
1. Add Student
2. Update Student Attendance
3. Display All Students
4. Show Average Attendance
5. Quit
Enter choice (1-5): 1
Enter student name: Sudip Timilsina
Enter attendance percentage: 50

--- Student Attendance System ---
Enter choice (1-5): 3
All Students:
ID: 1000, Name: Sudip Timilsina, Attendance: 50%
Notes
The program uses only basic Python constructs like classes, while loops, and lists.
No exception handling or advanced features are used — input must be valid (numbers for attendance and IDs).
Designed for learning purposes and small-scale prototypes.
