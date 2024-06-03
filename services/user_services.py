import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def create_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(255),
                password VARCHAR(255)
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(255),
            price INTEGER,
            quantity INTEGER,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)       
    )
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departament(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departament_name VARCHAR(255),
            product_id INTEGER,
            FOREIGN KEY(product_id) REFERENCES products(id)
    )
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        departament_id INTEGER,
        sale_date TIMESTAMP,
        quantity_sold INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(product_id) REFERENCES products(id),
        FOREIGN KEY(departament_id) REFERENCES departament(id)
)
""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS store(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        store_name VARCHAR(255),
        store_adress VARCHAR(255),
        manager_id INTEGER,
        FOREIGN KEY(manager_id) REFERENCES users(id)
    )
""")


create_table()