import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

d_id = 5

sql = """
    DELETE FROM clientes
    WHERE id = ?;
"""
parametro = (d_id)
cursor.execute(sql, parametro)
conexao.commit()
print('deletado com sucesso...')

conexao.close()