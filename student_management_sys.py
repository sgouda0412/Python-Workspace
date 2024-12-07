# Student Management System

# Variables
students = []  # List to hold student data as tuples
student_records = {}  # Dictionary to store student records by roll number


# Function to display the menu
def display_menu():
    print("\nStudent Management System")
    print("-" * 30)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Calculate Average Marks")
    print("5. Exit")


# Add a student
def add_student():
    roll_number = input("Enter Roll Number: ")
    if roll_number in student_records:
        print("❗ A student with this roll number already exists.")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    # Create a tuple and append it to the students list
    student = (roll_number, name, age, marks)
    students.append(student)

    # Add the student details to the dictionary
    student_records[roll_number] = {"Name": name, "Age": age, "Marks": marks}
    print("✅ Student added successfully!")


# View all students
def view_students():
    if not students:
        print("❗ No students found.")
        return

    print("\nStudent List:")
    print("-" * 30)
    for student in students:
        print(
            f"Roll Number: {student[0]}, Name: {student[1]}, Age: {student[2]}, Marks: {student[3]}",
            end="\n",
        )


# Search for a student by roll number
def search_student():
    roll_number = input("Enter Roll Number to search: ")
    if roll_number in student_records:
        print("\nStudent Details:")
        for key, value in student_records[roll_number].items():
            print(f"{key}: {value}", sep=", ")
    else:
        print("❌ Student not found.")


# Calculate average marks
def calculate_average_marks():
    if not students:
        print("❗ No students to calculate average marks.")
        return

    total_marks = sum(student[3] for student in students)  # Sum up all marks
    average_marks = total_marks / len(students)
    print(f"The average marks of all students is: {average_marks:.2f}")


# Main function
def main():
    while True:  # Infinite loop for menu
        display_menu()
        choice = input("Enter your choice: ")

        # Switch statement alternative
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average_marks()
        elif choice == "5":
            print("👋 Exiting Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# Entry point
if __name__ == "__main__":
    main()
