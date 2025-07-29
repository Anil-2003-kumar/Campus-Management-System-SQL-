import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_department(department_id, department_name, head_of_department, total_students):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO departments (department_id, department_name, head_of_department, total_students)
            VALUES (%s, %s, %s, %s)
        """, (department_id, department_name, head_of_department, total_students))
        conn.commit()
        print("✅ Department added.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_departments():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM departments")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_department(department_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departments WHERE department_id = %s", (department_id,))
    conn.commit()
    print("🗑️ Department deleted.")
    conn.close()

def update_department_head(department_id, new_hod):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE departments SET head_of_department = %s WHERE department_id = %s
    """, (new_hod, department_id))
    conn.commit()
    print("👨‍🏫 Department head updated.")
    conn.close()
