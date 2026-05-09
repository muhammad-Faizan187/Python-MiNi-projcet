# =================================================
#            Python Mini Database System
# =================================================

students = {}

while True:

    print("\n" + "=" * 40)
    print(" |   🎓 TEACHER RECORD SYSTEM 🎓   |")
    print("=" * 40)

    print("╔══════════════════════════════════╗")
    print("║  1 ➜ Add Student                 ║")
    print("║  2 ➜ View All Students           ║")
    print("║  3 ➜ Total Number of Students    ║")
    print("║  4 ➜ Search Student              ║")
    print("║  5 ➜ Delete Student              ║")
    print("║  6 ➜ Exit Program                ║")
    print("╚══════════════════════════════════╝")

    choice = input("\nEnter your choice: ")

    # =================================================
    # Add Student
    # =================================================
    if choice == "1":

        print("\n" + "-" * 40)
        print("         ADD NEW STUDENT")
        print("-" * 40)

        name = input("Enter student name : ")
        iD = input("Enter student ID   : ")

        students[name] = iD

        print("\n✅ Student Added Successfully!")
        print(f"👤 Name : {name}")
        print(f"🆔 ID   : {iD}")

    # =================================================
    # View All Students
    # =================================================
    elif choice == "2":

        print("\n" + "-" * 45)
        print("           ALL STUDENT RECORDS")
        print("-" * 45)

        if len(students) == 0:
            print("❌ No student records found Plz press 1 and student.")

        else:
            count = 1
            for name, iD in students.items():
                print(f"{count}. 👤 {name}  ➜  🆔 {iD}")
                count += 1

    # =================================================
    # Total Students
    # =================================================
    elif choice == "3":

        print("\n" + "-" * 40)
        print("         TOTAL STUDENTS")
        print("-" * 40)

        print(f"📚 Total Students = {len(students)}")

    # =================================================
    # Search Student
    # =================================================
    elif choice == "4":

        print("\n" + "-" * 40)
        print("         SEARCH STUDENT")
        print("-" * 40)

        search = input("Enter student name: ")

        if search in students:
            print("\n✅ Student Found")
            print(f"👤 Name : {search}")
            print(f"🆔 ID   : {students[search]}")
        else:
            print("❌ Student not found.")

    # =================================================
    # Delete Student
    # =================================================
    elif choice == "5":

        print("\n" + "-" * 40)
        print("         DELETE STUDENT")
        print("-" * 40)

        delete = input("Enter student name to delete: ")

        if delete in students:
            del students[delete]
            print("🗑️ Student deleted successfully.")
        else:
            print("❌ Student not found.")

    # =================================================
    # Exit Program
    # =================================================
    elif choice == "6":

        print("\n" + "=" * 55)
        print("      ❤️ Thanks For Using The Program ❤️")
        print("=" * 55)

        break

    # =================================================
    # Invalid Choice
    # =================================================
    else:
        print("\n❌ Invalid Choice! Please try again.")