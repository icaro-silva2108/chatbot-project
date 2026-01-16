from app.database.connection import get_conncetion

def create_reservation(user_id, destination_id, travel_date):
    try:
        conn = get_conncetion()
        cursor = conn.cursor()

        sql = "INSERT INTO reservations (user_id, destination_id, travel_date) VALUES (%s, %s, %s)"

        cursor.execute(sql, (user_id, destination_id, travel_date))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        conn.rollback()
        raise e

def cancel_reservation(reservation_id, email):

    try:
        conn = get_conncetion()
        cursor = conn.cursor()

        sql = "DELETE FROM reservations WHERE id = %s AND user_id = (SELECT id FROM users WHERE email = %s)"
        
        cursor.execute(sql, (reservation_id, email))
        
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        conn.rollback()
        raise e
