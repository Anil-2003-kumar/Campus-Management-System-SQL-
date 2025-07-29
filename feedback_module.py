import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_feedback(feedback_id, student_id, feedback_text, rating, feedback_date):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO feedback (feedback_id, student_id, feedback_text, rating, feedback_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (feedback_id, student_id, feedback_text, rating, feedback_date))
        conn.commit()
        print("✅ Feedback submitted.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_feedback():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_feedback(feedback_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedback WHERE feedback_id = %s", (feedback_id,))
    conn.commit()
    print("🗑️ Feedback deleted.")
    conn.close()
