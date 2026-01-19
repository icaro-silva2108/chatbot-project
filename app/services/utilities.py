from app.database.connection import get_connection

def search_user_by_email(email):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        email_query = "SELECT EXISTS(SELECT 1 FROM users WHERE email = %s)"
        cursor.execute(email_query, (email,))
        email_result = bool(cursor.fetchone()[0])# --> Garante que exista um usuário a ser buscado

        if email_result:

            id_query = "SELECT id FROM users WHERE email = %s;"
            cursor.execute(id_query, (email,))
            user_id = cursor.fetchone()[0]

            return user_id# --> Retorna o id do usuário buscado pelo email

        else:
            return None# --> Se não encontrar, retorna None

    except Exception as e:
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()