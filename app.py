from student_module import *
from room_module import *
from mess_module import *
from attendance_module import *
from feedback_module import *
from department_module import *
from course_module import *
from staff_module import *
from reports_module import *

def main():
    while True:
        print("\n📘 INTEGRATED CAMPUS RESOURCE MANAGER")
        print("1. Manage Students")
        print("2. Manage Rooms")
        print("3. Manage Mess Payments")
        print("4. Manage Attendance")
        print("5. Manage Feedback")
        print("6. Manage Departments")
        print("7. Manage Courses")
        print("8. Manage Staff")
        print("9. View Reports")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n-- Students --")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student Email")
            print("4. Delete Student")
            c = input("Enter option: ")
            if c == '1':
                sid = int(input("ID: "))
                name = input("Name: ")
                dept = input("Department: ")
                year = int(input("Year: "))
                email = input("Email: ")
                add_student(sid, name, dept, year, email)
            elif c == '2':
                view_students()
            elif c == '3':
                sid = int(input("Student ID: "))
                email = input("New Email: ")
                update_student_email(sid, email)
            elif c == '4':
                sid = int(input("Student ID: "))
                delete_student(sid)

        elif choice == '2':
            print("\n-- Rooms --")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Update Occupancy")
            print("4. Delete Room")
            c = input("Enter option: ")
            if c == '1':
                rid = int(input("Room ID: "))
                rno = input("Room Number: ")
                cap = int(input("Capacity: "))
                add_room(rid, rno, cap)
            elif c == '2':
                view_rooms()
            elif c == '3':
                rid = int(input("Room ID: "))
                occ = int(input("New Occupied Value: "))
                update_room_occupancy(rid, occ)
            elif c == '4':
                rid = int(input("Room ID: "))
                delete_room(rid)

        elif choice == '3':
            print("\n-- Mess Payments --")
            print("1. Add Payment")
            print("2. View Payments")
            print("3. Update Payment Status")
            print("4. Delete Payment")
            c = input("Enter option: ")
            if c == '1':
                pid = int(input("Payment ID: "))
                sid = int(input("Student ID: "))
                amt = float(input("Amount: "))
                date = input("Payment Date (YYYY-MM-DD): ")
                status = input("Status (Paid/Unpaid): ")
                add_payment(pid, sid, amt, date, status)
            elif c == '2':
                view_payments()
            elif c == '3':
                pid = int(input("Payment ID: "))
                status = input("New Status: ")
                update_payment_status(pid, status)
            elif c == '4':
                pid = int(input("Payment ID: "))
                delete_payment(pid)

        elif choice == '4':
            print("\n-- Attendance --")
            print("1. Add Attendance")
            print("2. View Attendance")
            print("3. Update Attendance Status")
            print("4. Delete Attendance")
            c = input("Enter option: ")
            if c == '1':
                aid = int(input("Attendance ID: "))
                sid = int(input("Student ID: "))
                date = input("Date (YYYY-MM-DD): ")
                status = input("Status (Present/Absent/Leave): ")
                add_attendance(aid, sid, date, status)
            elif c == '2':
                view_attendance()
            elif c == '3':
                aid = int(input("Attendance ID: "))
                status = input("New Status: ")
                update_attendance_status(aid, status)
            elif c == '4':
                aid = int(input("Attendance ID: "))
                delete_attendance(aid)

        elif choice == '5':
            print("\n-- Feedback --")
            print("1. Add Feedback")
            print("2. View Feedback")
            print("3. Delete Feedback")
            c = input("Enter option: ")
            if c == '1':
                fid = int(input("Feedback ID: "))
                sid = int(input("Student ID: "))
                text = input("Feedback Text: ")
                rating = int(input("Rating (1–5): "))
                date = input("Date (YYYY-MM-DD): ")
                add_feedback(fid, sid, text, rating, date)
            elif c == '2':
                view_feedback()
            elif c == '3':
                fid = int(input("Feedback ID: "))
                delete_feedback(fid)

        elif choice == '6':
            print("\n-- Departments --")
            print("1. Add Department")
            print("2. View Departments")
            print("3. Update HOD")
            print("4. Delete Department")
            c = input("Enter option: ")
            if c == '1':
                did = int(input("Department ID: "))
                dname = input("Name: ")
                hod = input("Head of Department: ")
                total = int(input("Total Students: "))
                add_department(did, dname, hod, total)
            elif c == '2':
                view_departments()
            elif c == '3':
                did = int(input("Department ID: "))
                new_hod = input("New HOD Name: ")
                update_department_head(did, new_hod)
            elif c == '4':
                did = int(input("Department ID: "))
                delete_department(did)

        elif choice == '7':
            print("\n-- Courses --")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Update Credits")
            print("4. Delete Course")
            c = input("Enter option: ")
            if c == '1':
                cid = int(input("Course ID: "))
                cname = input("Course Name: ")
                did = int(input("Department ID: "))
                credits = int(input("Credits: "))
                add_course(cid, cname, did, credits)
            elif c == '2':
                view_courses()
            elif c == '3':
                cid = int(input("Course ID: "))
                new_credits = int(input("New Credits: "))
                update_course_credits(cid, new_credits)
            elif c == '4':
                cid = int(input("Course ID: "))
                delete_course(cid)

        elif choice == '8':
            print("\n-- Staff --")
            print("1. Add Staff")
            print("2. View Staff")
            print("3. Update Staff Email")
            print("4. Delete Staff")
            c = input("Enter option: ")
            if c == '1':
                sid = int(input("Staff ID: "))
                name = input("Name: ")
                role = input("Role: ")
                dept = input("Department: ")
                email = input("Email: ")
                add_staff(sid, name, role, dept, email)
            elif c == '2':
                view_staff()
            elif c == '3':
                sid = int(input("Staff ID: "))
                new_email = input("New Email: ")
                update_staff_email(sid, new_email)
            elif c == '4':
                sid = int(input("Staff ID: "))
                delete_staff(sid)

        elif choice == '9':
            print("\n-- Reports --")
            print("1. Students per Department")
            print("2. Attendance %")
            print("3. Mess Dues")
            print("4. Avg. Feedback Rating")
            c = input("Enter option: ")
            if c == '1':
                total_students_per_department()
            elif c == '2':
                attendance_percentage()
            elif c == '3':
                mess_summary()
            elif c == '4':
                average_feedback_rating()

        elif choice == '0':
            print("👋 Exiting Campus Manager.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
