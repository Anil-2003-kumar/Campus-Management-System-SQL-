import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_course(course_id, course_name, department_id, credits):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO courses (course_id, course_name, department_id, credits)
            VALUES (%s, %s, %s, %s)
        """, (course_id, course_name, department_id, credits))
        conn.commit()
        print("✅ Course added.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_courses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_course(course_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
    conn.commit()
    print("🗑️ Course deleted.")
    conn.close()

def update_course_credits(course_id, new_credits):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE courses SET credits = %s WHERE course_id = %s
    """, (new_credits, course_id))
    conn.commit()
    print("🎓 Course credits updated.")
    conn.close()
