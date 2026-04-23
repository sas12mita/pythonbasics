#student Management System (Assessment 1) 
students=[] #list which hold all student's records
student_ids=set() # set  used to store unique student id
 
while True:
    print("=====Student Management System====")
    print("1. Add Student Records")
    print("2. View Student Records")
    print("3. Search Student")
    print("4. Delete Student Record")
    print("5. Exit")
    choice =input("Enter number from 1 to 5 to choose operation: ")

    #Add student if user press 1
    if choice =="1":
        name=input("Enter student name: ")
        sid=(input("Enter student ID: "))
        mark=int(input("Enter marks in numeric form: "))
        
        # check duplicate of student id using
        if sid in student_ids:
            print("Student ID already Exists\n")
            continue
        # check validation of mark
        if mark < 0 or mark >100:
            print("Invalid Mark!! Please enter mark between 0 to 100\n")
            continue

        #Grade categorization
        if mark < 50:
            grade ="F"
        elif mark < 65:
            grade ="P"
        elif mark < 75:
            grade ="C"
        elif mark < 85:
            grade ="D"
        else:
            grade ="HD"
        
        #add student detail to list students using append method
        students.append((name,sid,mark,grade)) 

        # add student id to set student_ids which remove duplicate of 
        student_ids.add(sid)
        print("student added successfully\n")

    #view all student record
    elif choice =='2':
        if not students:
            print("No records Found!! enter 1 to add student first ")

        else: 
            for student in students:
                name,sid, mark,grade=student
                print(f"Student name:{name}, Student ID:{sid}, Mark:{mark}, Grade:{grade}")
            print()

    #chatgpt suggest me to do search operation
    #Search particular student record
    elif choice=="3":
        sid = input("Please enter student id to search: ")
        found = False

        for student in students: #loops through all student record
            if student[1] == sid: # check if  entred ID  match to Id store  in list or not
                name, sid, mark, grade = student
                print(f"Student Name: {name}, Student ID: {sid}, Mark: {mark}, Grade: {grade}\n")
                found = True
                break

        if not found:
            print("Searched student not found.\n")

   #delete particular student
    elif choice=="4":
        sid=input("Enter student ID to delete student record: ")
        for student in students: #loops through all student record
            if student[1]==sid: # check if  entred ID  match to Id store  in list or not
                students.remove(student) #revove student 
                student_ids.remove(sid)#remove student ID from set
                print("Student deleted sucessfully\n")
                break
        else:
            print("student not found\n")

    #exiting program
    elif choice == "5":
        print("exiting program...")
        break
    else:
        print("invalid choice.Try try again")#invalid choice

    


        
        



