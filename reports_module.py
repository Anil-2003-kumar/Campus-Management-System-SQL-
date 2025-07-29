import mysql.connector
import numpy as np

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def total_students_per_department():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT department, COUNT(*) FROM students GROUP BY department")
    result = cursor.fetchall()
    print("\n🎓 Total Students per Department:")
    for dept, count in result:
        print(f"{dept}: {count}")
    conn.close()

def attendance_percentage():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT student_id, 
               SUM(CASE WHEN status='Present' THEN 1 ELSE 0 END) AS present_days,
               COUNT(*) AS total_days
        FROM attendance
        GROUP BY student_id
    """)
    print("\n📋 Attendance Percentage:")
    for student_id, present, total in cursor.fetchall():
        percentage = (present / total) * 100 if total > 0 else 0
        print(f"Student {student_id}: {percentage:.2f}%")
    conn.close()

def mess_summary():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT student_id, SUM(amount) FROM mess_payments WHERE status != 'Paid' GROUP BY student_id
    """)
    result = cursor.fetchall()
    print("\n🍽️ Unpaid Mess Dues:")
    for student_id, due in result:
        print(f"Student {student_id}: ₹{due}")
    conn.close()

def average_feedback_rating():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(rating) FROM feedback")
    avg_rating = cursor.fetchone()[0]
    print(f"\n⭐ Average Feedback Rating: {avg_rating:.2f}/5")
    conn.close()
