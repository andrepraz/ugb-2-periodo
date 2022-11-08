import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

p_nome = 'André'
p_idade = 48

sql = """
    INSERT INTO clientes (nome, idade)
    VALUES (?, ?);
"""

parametro = (p_nome, p_idade)

cursor.execute(sql, parametro)
conexao.commit()
print('salvo com sucesso...')
conexao.close()