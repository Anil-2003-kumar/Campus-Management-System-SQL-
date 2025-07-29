import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_staff(staff_id, name, role, department, contact_email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO staff (staff_id, name, role, department, contact_email)
            VALUES (%s, %s, %s, %s, %s)
        """, (staff_id, name, role, department, contact_email))
        conn.commit()
        print("✅ Staff member added.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_staff():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_staff(staff_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
    conn.commit()
    print("🗑️ Staff member deleted.")
    conn.close()

def update_staff_email(staff_id, new_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE staff SET contact_email = %s WHERE staff_id = %s
    """, (new_email, staff_id))
    conn.commit()
    print("📧 Staff email updated.")
    conn.close()
