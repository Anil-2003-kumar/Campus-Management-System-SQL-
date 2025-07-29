import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_payment(payment_id, student_id, amount, payment_date, status):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO mess_payments (payment_id, student_id, amount, payment_date, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (payment_id, student_id, amount, payment_date, status))
        conn.commit()
        print("✅ Mess payment added successfully.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_payments():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mess_payments")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_payment_status(payment_id, new_status):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE mess_payments SET status = %s WHERE payment_id = %s
    """, (new_status, payment_id))
    conn.commit()
    print("💳 Payment status updated.")
    conn.close()

def delete_payment(payment_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mess_payments WHERE payment_id = %s", (payment_id,))
    conn.commit()
    print("🗑️ Payment record deleted.")
    conn.close()
