from auth import login_user, register_user
from crud import add_grade, list_grades

def main_menu():
    print("\n1. Login")
    print("2. Registrar Aluno")
    print("3. Registrar Professor")
    print("4. Sair")
    return input("Escolha uma opção: ")

def user_menu(user_type):
    print("\n1. Adicionar Nota" if user_type == "professor" else "1. Ver Minhas Notas")
    print("2. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        choice = main_menu()

        if choice == "1":
            matricula = input("Matrícula: ")
            senha = input("Senha: ")
            user_type = input("Tipo de usuário (aluno/professor): ").lower()

            if login_user(matricula, senha, user_type):
                print(f"\nBem-vindo, {user_type}!")
                
                while True:
                    option = user_menu(user_type)

                    if option == "1":
                        if user_type == "professor":
                            matricula_aluno = input("Matrícula do aluno: ")
                            disciplina = input("Disciplina: ")
                            nota = float(input("Nota: "))
                            add_grade(matricula_aluno, matricula, disciplina, nota)
                        else:
                            list_grades(matricula)
                    elif option == "2":
                        print("Saindo...")
                        break
            else:
                print("Matrícula ou senha incorreta.")

        elif choice == "2":
            print("\n--- Cadastro de Aluno ---")
            matricula = input("Matrícula: ")
            nome = input("Nome: ")
            senha = input("Senha: ")
            register_user(matricula, nome, senha, "aluno")

        elif choice == "3":
            print("\n--- Cadastro de Professor ---")
            matricula = input("Matrícula: ")
            nome = input("Nome: ")
            senha = input("Senha: ")
            register_user(matricula, nome, senha, "professor")

        elif choice == "4":
            print("Encerrando o sistema...")
            break

if __name__ == "__main__":
    main()
