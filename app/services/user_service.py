from app.database.connection import get_connection

"""
Variáveis 'conn'(conexão ao banco) e 'cursor'(meio entre python e banco) recebendo None servem de garantia para que elas existam e não quebrem o código.
A variável 'sql' é um código sql a ser executado pelo comando cursor.execute(...)
A variável 'sql' possui Placeholders(%s) contra sql injection
conn.comit() acompanha o cursor.execute() para salvar as alterações feitas no database
Blocos finally servem para garantir que a conexão e o cursor serão interrompidos, impedindo acesso desnecessário ao banco e consumo de memória.
Blocos except tratam o retorno do database a um estado estável com rollback e apresenta o erro ocorrido
"""

def create_user(name, email, password_hash, birth_date):# --> Criação de novo usuário

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        email_query = "SELECT EXISTS(SELECT 1 FROM users WHERE email = %s)"# --> Query separada para verificar se o emil já existe
        cursor.execute(email_query, (email,))
        result_query = bool(cursor.fetchone()[0])

        if not result_query:
            sql = "INSERT INTO users (name, email, password_hash, birth_date) VALUES (%s, %s, %s, %s);"
            cursor.execute(sql, (name, email, password_hash, birth_date))

            conn.commit()
            return True# --> Se não existir, confirma que o usuário foi criado

        else:
            return False# --> Se existir, não poderá criar um usuário com o mesmo email

    except Exception as e:
        if conn:
            conn.rollback()
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_user(email):# --> Exclui o cadastro do usuário

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        id_query = "SELECT id FROM users WHERE email = %s;"
        cursor.execute(id_query, (email,))
        user_id = cursor.fetchone()[0]

        rows_select = ("SELECT COUNT(*) FROM reservations WHERE user_id = %s;")
        cursor.execute(rows_select, (user_id,))
        rows = cursor.fetchone()[0]#--> Verifica se o usuário tem reservas

        if user_id and rows < 1:    

            sql = ("DELETE FROM users WHERE id = %s;")

            cursor.execute(sql, (user_id,))
            
            conn.commit()
            return True# --> Se usuário não tiver reservas, confirma que teve o cadastro excluído

        else:
            return False# --> Se tiver, mostra que não foi possível ser excluído e deve deletar as reservas antes

    except Exception as e:
        if conn:
            conn.rollback()
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()