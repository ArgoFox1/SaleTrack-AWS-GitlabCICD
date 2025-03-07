import sqlite3

DATABASE = 'sales.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_sale(product_name, quantity, price, description):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sales (product_name, quantity, price, description)
        VALUES (?, ?, ?, ?)
    ''', (product_name, quantity, price, description))
    conn.commit()
    conn.close()

def get_daily_sales():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sales WHERE DATE(timestamp) = DATE("now")')
    sales = cursor.fetchall()
    conn.close()
    total_revenue = sum(row[2] * row[3] for row in sales) if sales else 0
    return sales, total_revenue
