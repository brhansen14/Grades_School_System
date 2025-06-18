from database import connect_db

def add_grade(matricula_aluno, matricula_professor, disciplina, nota):
    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute("""
            INSERT INTO notas (matricula_aluno, matricula_professor, disciplina, nota) 
            VALUES (%s, %s, %s, %s)
        """, (matricula_aluno, matricula_professor, disciplina, nota))
        db.commit()
        print("Nota adicionada com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar nota: {e}")
    finally:
        cursor.close()
        db.close()

def update_grade(nota_id, nova_nota):
    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute("""
            UPDATE notas 
            SET nota = %s 
            WHERE id = %s
        """, (nova_nota, nota_id))
        db.commit()
        print("Nota atualizada com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar nota: {e}")
    finally:
        cursor.close()
        db.close()

def delete_grade(nota_id):
    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute("DELETE FROM notas WHERE id = %s", (nota_id,))
        db.commit()
        print("Nota removida com sucesso.")
    except Exception as e:
        print(f"Erro ao remover nota: {e}")
    finally:
        cursor.close()
        db.close()

def list_grades(matricula_aluno):
    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT disciplina, nota FROM notas WHERE matricula_aluno = %s", (matricula_aluno,))
        results = cursor.fetchall()
        for disciplina, nota in results:
            print(f"Disciplina: {disciplina} - Nota: {nota}")
    except Exception as e:
        print(f"Erro ao listar notas: {e}")
    finally:
        cursor.close()
        db.close()
