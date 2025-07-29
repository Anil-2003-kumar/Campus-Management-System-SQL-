import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="campus_db"
    )

def add_room(room_id, room_number, capacity):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO rooms (room_id, room_number, capacity)
            VALUES (%s, %s, %s)
        """, (room_id, room_number, capacity))
        conn.commit()
        print("✅ Room added successfully.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def view_rooms():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_room_occupancy(room_id, new_occupied):
    conn = connect()
    cursor = conn.cursor()
    try:
        is_available = new_occupied < cursor.execute("SELECT capacity FROM rooms WHERE room_id = %s", (room_id,))
        cursor.execute("""
            UPDATE rooms
            SET occupied = %s,
                is_available = %s
            WHERE room_id = %s
        """, (new_occupied, is_available, room_id))
        conn.commit()
        print("🛏️ Room occupancy updated.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        conn.close()

def delete_room(room_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rooms WHERE room_id = %s", (room_id,))
    conn.commit()
    print("🗑️ Room deleted.")
    conn.close()
