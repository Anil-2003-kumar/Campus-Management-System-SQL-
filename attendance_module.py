import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_attendance(attendance_id, student_id, date, status):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO attendance (attendance_id, student_id, date, status)
            VALUES (%s, %s, %s, %s)
        """, (attendance_id, student_id, date, status))
        conn.commit()
        print("✅ Attendance record added.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_attendance():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_attendance_status(attendance_id, new_status):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE attendance SET status = %s WHERE attendance_id = %s
    """, (new_status, attendance_id))
    conn.commit()
    print("📋 Attendance status updated.")
    conn.close()

def delete_attendance(attendance_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM attendance WHERE attendance_id = %s", (attendance_id,))
    conn.commit()
    print("🗑️ Attendance record deleted.")
    conn.close()
