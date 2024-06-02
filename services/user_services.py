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


create_table()