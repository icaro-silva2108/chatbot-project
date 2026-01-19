from app.database.connection import get_connection
from app.services.utilities import search_user_by_email

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

        user_id = search_user_by_email(email)
        if not user_id:
            return False
        
        rows_select = ("SELECT COUNT(*) FROM reservations WHERE user_id = %s;")
        cursor.execute(rows_select, (user_id,))
        rows = cursor.fetchone()[0]#--> Verifica se o usuário tem reservas

        if rows < 1:    

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

def change_user_info(email, info: dict):# --> Altera informações de cadastro do usuário que forem permitidas
    
    conn = None
    cursor = None

    allowed_keys = {"name", "email", "password_hash", "birth_date"}# --> Chaves permitidas

    try:
        conn = get_connection()
        cursor = conn.cursor()

        user_id = search_user_by_email(email)

        keys_to_change = []# --> Guardas os nome das chaves(colunas do database) para serem aplicadas no sql
        new_values = []# --> Guarda os novos valores que vão substituir os antigos do database
        sql_string = ""# --> String para auxiliar na execuçõa do comando sql

        if info:
            for key, value in info.items():
                if key in allowed_keys:# --> Só serão substituiádos os registros de colunas permitidas
                    keys_to_change.append(key)
                    new_values.append(value)

            if not keys_to_change:
                return False# --> Se não houver colunas para alterar, mostra que não foi possível fazer alterações

            sql_string = ",".join(f"{key} = %s" for key in keys_to_change)# --> Monta a string de forma adequada para executar o comando sql

            sql =f"""UPDATE users
                    SET {sql_string}
                    WHERE id = %s"""

            new_values.append(user_id)# --> Adiciona o id do usuário no fim da lista dos valores para facilitar no uso do Placeholder

            cursor.execute(sql, (tuple(new_values),))
            conn.commit()
            return True# --> Retorna que as alterações foram executadas com sucesso

        else:
            return False# --> Se não houver nada no para modificar, mostra que não foi possível fazer as alterações



    except Exception as e:
        if conn:
            conn.rollback()
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()