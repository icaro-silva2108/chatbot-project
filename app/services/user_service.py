from app.database.connection import get_conncetion

def create_user(name, email, password_hash, birth_date):
    conn = get_conncetion()
    cursor = conn.cursor()
        
    sql = "INSERT INTO users (name, email, password_hash, birth_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, password_hash, birth_date))
    
    conn.commit()
    cursor.close()
    conn.close()
