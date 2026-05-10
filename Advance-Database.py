# =========================================================
#        ADVANCED TEACHER RECORD SYSTEM (FILE HANDLING)
# =========================================================

import json
import os

# =========================================================
# File Name
# =========================================================
FILE_NAME = "students_data.json"

# =========================================================
# Load Data
# =========================================================
if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r") as file:

        try:
            students = json.load(file)

        except:
            students = {}

else:
    students = {}

# =========================================================
# Save Data Function
# =========================================================
def save_data():

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# =========================================================
# Main Program
# =========================================================


print("\n" + "=" * 40)
print("| 🎓 ADVANCED TEACHER RECORD SYSTEM 🎓|")
print("=" * 40)

print("""
╔══════════════════════════════════════╗
║  1 ➜ Add Student                     ║
║  2 ➜ View All Students               ║
║  3 ➜ Total Number of Students        ║
║  4 ➜ Search Student                  ║
║  5 ➜ Delete Student                  ║
║  6 ➜ Update Student                  ║
║  7 ➜ Clear All Records               ║
║  8 ➜ Sort Student Names              ║
║  9 ➜ Check Student Exists            ║
║ 10 ➜ Backup Database File            ║
║ 11 ➜ Exit Program                    ║
╚══════════════════════════════════════╝
""")
while True:

    choice = input("Enter your choice: ")

    # =====================================================
    # Add Student
    # =====================================================
    if choice == "1":

        print("\n----- ADD STUDENT -----")

        name = input("Enter student name : ")
        iD = input("Enter student ID   : ")

        if name in students:
            print("❌ Student already exists.")

        else:
            students[name] = iD
            save_data()

            print("✅ Student Added Successfully!")

    # =====================================================
    # View Students
    # =====================================================
    elif choice == "2":

        print("\n----- ALL STUDENTS -----")

        if len(students) == 0:
            print("❌ No student records found.")

        else:

            count = 1

            for name, iD in students.items():

                print(f"{count}. 👤 {name} ➜ 🆔 {iD}")
                count += 1

    # =====================================================
    # Total Students
    # =====================================================
    elif choice == "3":

        print("\n----- TOTAL STUDENTS -----")

        print(f"📚 Total Students = {len(students)}")

    # =====================================================
    # Search Student
    # =====================================================
    elif choice == "4":

        print("\n----- SEARCH STUDENT -----")

        search = input("Enter student name: ")

        if search in students:

            print("✅ Student Found")
            print(f"👤 Name : {search}")
            print(f"🆔 ID   : {students[search]}")

        else:
            print("❌ Student not found.")

    # =====================================================
    # Delete Student
    # =====================================================
    elif choice == "5":

        print("\n----- DELETE STUDENT -----")

        delete = input("Enter student name to delete: ")

        if delete in students:

            del students[delete]

            save_data()

            print("🗑️ Student deleted successfully.")

        else:
            print("❌ Student not found.")

    # =====================================================
    # Update Student
    # =====================================================
    elif choice == "6":

        print("\n----- UPDATE STUDENT -----")

        old_name = input("Enter old student name: ")

        if old_name in students:

            new_name = input("Enter new student name: ")
            new_id = input("Enter new student ID: ")

            del students[old_name]

            students[new_name] = new_id

            save_data()

            print("✅ Student updated successfully.")

        else:
            print("❌ Student not found.")

    # =====================================================
    # Clear All Records
    # =====================================================
    elif choice == "7":

        print("\n⚠️ WARNING!")
        confirm = input("Do you want to delete ALL records? (yes/no): ")

        if confirm.lower() == "yes":

            students.clear()

            save_data()

            print("🗑️ All records deleted.")

        else:
            print("❌ Operation cancelled.")

    # =====================================================
    # Sort Student Names
    # =====================================================
    elif choice == "8":

        print("\n----- SORTED STUDENTS -----")

        if len(students) == 0:
            print("❌ No records found.")

        else:

            count = 1

            for name in sorted(students):

                print(f"{count}. 👤 {name} ➜ 🆔 {students[name]}")
                count += 1

    # =====================================================
    # Check Student Exists
    # =====================================================
    elif choice == "9":

        print("\n----- CHECK STUDENT -----")

        check = input("Enter student name: ")

        if check in students:
            print("✅ Student exists in database.")

        else:
            print("❌ Student does not exist.")

    # =====================================================
    # Backup Database
    # =====================================================
    elif choice == "10":

        backup_file = "backup_students_data.json"

        with open(backup_file, "w") as file:

            json.dump(students, file, indent=4)

        print("✅ Backup file created successfully.")

    # =====================================================
    # Exit Program
    # =====================================================
    elif choice == "11":

        print("\n" + "=" * 55)
        print("      ❤️ Thanks For Using The Program ❤️")
        print("=" * 55)

        break

    # =====================================================
    # Invalid Choice
    # =====================================================
    else:

        print("❌ Invalid Choice! Please try again.")