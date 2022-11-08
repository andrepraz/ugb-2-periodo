import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    );
"""
cursor.execute(sql)
print('Tabela criada...')

conexao.close()