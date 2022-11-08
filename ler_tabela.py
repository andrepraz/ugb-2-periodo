import sqlite3
conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = '''select * from clientes;'''

cursor.execute(sql)
resultado = cursor.fetchall()
print('resultado',resultado)

for i in resultado:
    print(i)

conexao.close()