import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        port = '3306',
        user="root",
        password="",
        database="school_db"
    )

def create_tables():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INT PRIMARY KEY,
            nome VARCHAR(100),
            senha VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            matricula INT PRIMARY KEY,
            nome VARCHAR(100),
            senha VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            matricula_aluno INT,
            matricula_professor INT,
            disciplina VARCHAR(100),
            nota DECIMAL(5, 2),
            FOREIGN KEY (matricula_aluno) REFERENCES alunos(matricula),
            FOREIGN KEY (matricula_professor) REFERENCES professores(matricula)
        );
    """)

    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    create_tables()
