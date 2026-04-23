# Student Management System (Final Optimised Version)

students = []       # list of tuples: (name, id, marks, grade)
student_ids = set() # set to track unique IDs

while True:
    print("==== Student Management System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        name = input("Enter student name: ")
        sid = input("Enter student ID: ")
        mark = int(input("Enter marks: "))

        # Check duplicate using set
        if sid in student_ids:
            print("Student ID already exists!\n")
            continue

        # Validate marks
        if mark < 0 or mark > 100:
            print("Invalid marks! Must be 0 to 100.\n")
            continue

        # Grade calculation
        if mark < 50:
            grade = "F"
        elif mark < 65:
            grade = "P"
        elif mark < 75:
            grade = "C"
        elif mark < 85:
            grade = "D"
        else:
            grade = "HD"

        students.append((name, sid, mark, grade))
        student_ids.add(sid)

        print("Student added successfully!\n")

    # View Students
    elif choice == '2':
        if not students:
            print("No records found.\n")
        else:
            for student in students:
                name, sid, mark, grade = student
                print(f"Name: {name}, ID: {sid}, Marks: {mark}, Grade: {grade}")
            print()

    # Search Student
    elif choice == '3':
        sid = input("Enter student ID to search: ")
        found = False

        for student in students:
            if student[1] == sid:
                name, sid, mark, grade = student
                print(f"Found -> Name: {name}, ID: {sid}, Marks: {mark}, Grade: {grade}\n")
                found = True
                break

        if not found:
            print("Student not found.\n")

    # Update Student
    elif choice == '4':
        sid = input("Enter student ID to update: ")

        for i in range(len(students)):
            if students[i][1] == sid:
                name, sid, _, _ = students[i]
                new_mark = int(input("Enter new marks: "))

                if new_mark < 0 or new_mark > 100:
                    print("Invalid marks!\n")
                    break

                # Recalculate grade
                if new_mark < 50:
                    grade = "F"
                elif new_mark < 65:
                    grade = "P"
                elif new_mark < 75:
                    grade = "C"
                elif new_mark < 85:
                    grade = "D"
                else:
                    grade = "HD"

                students[i] = (name, sid, new_mark, grade)
                print("Student updated successfully!\n")
                break
        else:
            print("Student not found.\n")

    # Delete Student
    elif choice == '5':
        sid = input("Enter student ID to delete: ")

        for student in students:
            if student[1] == sid:
                students.remove(student)
                student_ids.remove(sid)
                print("Student deleted succes1sfully!\n")
                break
        else:
            print("Student not found.\n")

    # Exit
    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.\n")