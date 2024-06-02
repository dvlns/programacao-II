import sqlite3
import bcrypt

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def criptografar(password):
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed

def check_password(password, hashed):
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)

def user_register(email, password):
    password = criptografar(password)
    cursor.execute("""
        INSERT INTO users(email, password) VALUES (?, ?)
""",[email, password])
    connection.commit()
    
def login(email, password):
    sql = "SELECT email, password FROM users WHERE email=?"
    user = cursor.execute(sql, [email]).fetchone()
    if user:
        email, hashed = user
        if check_password(password, hashed):
            sql = "SELECT id FROM users WHERE email=?"
            global usuario_atual
            resultado = cursor.execute(sql,[email]).fetchone()
            usuario_atual = resultado[0]
            tela_sistema()  
        else:
            print("Senha incorreta") 
    else:
        print("Usuário não encontrado")

def cadastrar():
    produto = input("Digite o produto: ")
    
    while True:
        try:
            preco = int(input("Digite o preço: "))
            break
        except ValueError:
            print("Valor inválido")
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            break
        except ValueError:
            print("Valor inválido")
    
    cursor.execute("""
    INSERT INTO products(product_name, price, quantity, user_id) VALUES (?, ?, ?, ?)
    """,[produto, preco, quantidade, usuario_atual])
    connection.commit()  

def remover_produto():
    id = input("Digite o id do produto a ser removido: ")
    cursor.execute("DELETE FROM products WHERE id=?", (id))
    connection.commit()

def ler_produtos():
    sql = "SELECT * FROM products"
    cursor.execute(sql)
    
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"Produto: {produto[1]}")
        print(f"Preço: R${produto[2]}")
        print(f"Quantidade: {produto[3]}")
        print("--------------------")

def atualizar_produto():
    id = int(input("Digite o ID do produto a ser atualizado: "))
    produto = input("Digite o novo nome do produto: ")
    while True:
        try:
            preco = int(input("Digite o novo preço: "))
            break
        except ValueError:
            print("Valor inválido")
    while True:
        try:
            quantidade = int(input("Digite a nova quantidade: "))
            break
        except ValueError:
            print("Valor inválido")

    cursor.execute("""
    UPDATE products
    SET product_name = ?, price = ?, quantity = ?
    WHERE id=?;
    """,[produto, preco, quantidade, id])
    connection.commit()

def busca():
    busca = input("Digite o nome do produto a ser buscado: ")
    
    consulta = "SELECT product_name FROM products WHERE product_name LIKE ?"
    resultados = cursor.execute(consulta, ('%' + busca + '%',)).fetchall()
    for i in resultados:
        print(i[0]) 

def tela_sistema():
    while True:
        print("""
1 - Cadastrar produto
2 - Atualizar produto
3 - Ver produtos
4 - Remover produto
5 - Buscar produto
6 - Sair do sistema""")
        while True:
            try:
                choice = int(input(""))
                break
            except ValueError:
                print("Valor inválido")
        if choice == 1:
            cadastrar()
        elif choice == 2:
            atualizar_produto()
        elif choice == 3:
            ler_produtos()
        elif choice == 4:
            remover_produto()
        elif choice == 5:
            busca()
        elif choice == 6:
            break
        else:
            print("Opção inválida")

        



