class Student:
    nextID = 1000
    allStudents = []

    # Constructor: automatically assigns ID and stores student
    def __init__(self, name, attendance):
        self.studentName = name
        self.studentAttendance = attendance
        self.studentID = Student.nextID
        Student.nextID += 1
        Student.allStudents.append(self)

    # Add a new student interactively
    def addStudent(self):
        name = input("Enter student name: ")
        attendance = float(input("Enter attendance percentage: "))
        Student(name, attendance)  # automatically stored

    # Display all students
    def displayStudents(self):
        if len(Student.allStudents) == 0:
            print("No students added yet.")
            return
        print("\nAll Students:")
        index = 0
        while index < len(Student.allStudents):
            s = Student.allStudents[index]
            print("ID:", s.studentID, "Name:", s.studentName, "Attendance:", s.studentAttendance)
            index += 1

    # Update a student's attendance by ID
    def updateStudent(self):
        if len(Student.allStudents) == 0:
            print("No students to update.")
            return
        student_id = int(input("Enter student ID to update: "))
        index = 0
        found = False
        while index < len(Student.allStudents):
            s = Student.allStudents[index]
            if s.studentID == student_id:
                new_attendance = float(input("Enter new attendance for " + s.studentName + ": "))
                s.studentAttendance = new_attendance
                print("Attendance updated for", s.studentName)
                found = True
            index += 1
        if found == False:
            print("Student ID not found.")

    # Calculate average attendance
    def averageAttendance(self):
        if len(Student.allStudents) == 0:
            print("No students to calculate average.")
            return
        total = 0
        index = 0
        while index < len(Student.allStudents):
            total += Student.allStudents[index].studentAttendance
            index += 1
        average = total / len(Student.allStudents)
        print("Average Attendance:", average)


# ------------------------
# Interactive program
# ------------------------

# Start directly without a dummy
studentsController = Student("FirstStudentPlaceholder", 0)  # placeholder is immediately overwritten
Student.allStudents.pop()  # remove the placeholder, we just need the object to call methods

while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Update Student Attendance")
    print("3. Display All Students")
    print("4. Show Average Attendance")
    print("5. Quit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        studentsController.addStudent()
    elif choice == "2":
        studentsController.updateStudent()
    elif choice == "3":
        studentsController.displayStudents()
    elif choice == "4":
        studentsController.averageAttendance()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")