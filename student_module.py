import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_student(student_id, name, department, year, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_id, name, department, year, email) VALUES (%s, %s, %s, %s, %s)",
                       (student_id, name, department, year, email))
        conn.commit()
        print("✅ Student added successfully.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_student(student_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    print("🗑️ Student deleted successfully.")
    conn.close()

def update_student_email(student_id, new_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    print("✉️ Student email updated.")
    conn.close()
