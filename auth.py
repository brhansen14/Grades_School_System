import hashlib
from database import connect_db

def hash_password(password):
    """Gera o hash da senha."""
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(matricula, senha, user_type):
    """Realiza o login do usuário (aluno ou professor)."""
    db = connect_db()
    cursor = db.cursor()

    table = "alunos" if user_type == "aluno" else "professores"
    query = f"SELECT senha FROM {table} WHERE matricula = %s"
    cursor.execute(query, (matricula,))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result and result[0] == hash_password(senha):
        return True
    return False

def register_user(matricula, nome, senha, user_type):
    """Registra um novo aluno ou professor."""
    db = connect_db()
    cursor = db.cursor()

    table = "alunos" if user_type == "aluno" else "professores"

    # Verificar se a matrícula já está cadastrada
    cursor.execute(f"SELECT matricula FROM {table} WHERE matricula = %s", (matricula,))
    if cursor.fetchone():
        print(f"Erro: A matrícula {matricula} já está cadastrada como {user_type}.")
        cursor.close()
        db.close()
        return

    try:
        query = f"INSERT INTO {table} (matricula, nome, senha) VALUES (%s, %s, %s)"
        cursor.execute(query, (matricula, nome, hash_password(senha)))
        db.commit()
        print(f"{user_type.capitalize()} cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar {user_type}: {e}")
    finally:
        cursor.close()
        db.close()
