class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class AttendanceRecord:
    def __init__(self, date, present):
        self.date = date
        self.present = present

class AttendanceManagementSystem:
    def __init__(self):
        self.students = []
        self.attendance_records = {}

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        student = Student(id, name)
        self.students.append(student)
        self.attendance_records[id] = []
        print("Student added successfully!")

    def mark_attendance(self):
        id = input("Enter student ID: ")
        if id not in self.attendance_records:
            print("Student not found!")
            return

        date = input("Enter date (YYYY-MM-DD): ")
        present = input("Present? (y/n): ").lower() == 'y'
        record = AttendanceRecord(date, present)
        self.attendance_records[id].append(record)
        print("Attendance marked successfully!")

    def display_records(self):
        for student in self.students:
            print(f"Student: {student.name} (ID: {student.id})")
            for record in self.attendance_records[student.id]:
                print(f"  Date: {record.date}, Present: {record.present}")
            print()

    def run(self):
        while True:
            print("\nAttendance Management System")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. Display Records")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.mark_attendance()
            elif choice == '3':
                self.display_records()
            elif choice == '4':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ams = AttendanceManagementSystem()
    ams.run()