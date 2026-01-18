from app.database.connection import get_connection

def show_reservations():

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "SELECT city, country, description, price FROM destinations;"
        cursor.execute(sql)
        results = cursor.fetchall()

        return results
    
    except Exception as e:
        raise e
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()