# Week 7 Labs - IT5016 Assessment 3

This folder contains Python lab exercises for Week 7 of IT5016, focusing on **object-oriented programming (OOP)** concepts and **student management systems**.  
The exercises help students practice working with classes, objects, methods, and interactive program design.

---

## File Description

**studentmanagement.py**  
This program implements a simple student attendance management system. It demonstrates OOP concepts and provides functionality to manage students and their attendance percentages.

---

## Features of the Program

- **Student Class**:  
  - Stores student name, attendance percentage, and a unique auto-incrementing student ID.  
  - Maintains a list of all students added to the system.  

- **Methods in Student Class**:  
  - `addStudent()`: Add a new student with name and attendance interactively.  
  - `displayStudents()`: Show a list of all students with their IDs, names, and attendance percentages.  
  - `updateStudent()`: Update attendance for a specific student by entering their ID.  
  - `averageAttendance()`: Calculate and display the average attendance of all students.

- **Interactive Menu**:  
  - Provides options to:
    1. Add a student  
    2. Update student attendance  
    3. Display all students  
    4. Show average attendance  
    5. Quit the program  
  - The menu repeats until the user chooses to exit.

---

## How to Run the Program

1. Make sure Python 3.x is installed.  
2. Open a terminal or command prompt and navigate to the folder containing `studentmanagement.py`.  
3. Run the program using Python:
