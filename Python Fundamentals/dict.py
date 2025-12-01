students={
    "priya":34,
    "nidhi":58,
    "Omkar":90,
}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    # 1. Add a student
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # 2. Update marks
    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # 3. Search a student
    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} → {students[name]} marks")
        else:
            print("Student not found!")

    # 4. Display all students
    elif choice == 'D':
        if len(students) == 0:
            print("No students in the dictionary.")
        else:
            print("\n--- All Students ---")
            for name, marks in students.items():
                print(f"{name} : {marks}")

    # 5. Exit program
    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")
