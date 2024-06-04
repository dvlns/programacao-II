from utils.user_utils import login, user_register
from services.user_services import create_tables

def main():
    create_tables()
    while True:
        print("""
1 - Login 
2 - Registrar 
3 - Sair """)
        while True:
            try:
                choice = int(input(""))
                break
            except ValueError:
                print("Valor inválido")
        if choice == 1:
            email = input("Insira email: ")
            password = input("Insira senha: ")
            login(email, password)
        if choice == 2:
            email = input("Insira email: ")
            password = input("Insira senha: ")
            user_register(email, password)
        if choice == 3:
            break
            


main()
