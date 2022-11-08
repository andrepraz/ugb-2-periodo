import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

a_nome = 'maria'
a_idade = 21

p_id = 2

sql = """
    UPDATE clientes
    SET nome = ?, idade = ?
    WHERE id = ?;
"""
parametro = (a_nome, a_idade, p_id)

cursor.execute(sql, parametro)
conexao.commit()
print("alterado com sucesso...")
conexao.close()