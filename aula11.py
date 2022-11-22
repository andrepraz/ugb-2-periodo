'''
autor: Andre
Data: 21/11/2022
'''

from crud_firebase import CrudFirebase
crud = CrudFirebase()

while True:
    print('''
    Escolha uma opção:
    1 - incluir
    2 - ler
    3 - alterar
    4 - deletar
    5 - sair
    ''')
    valor = input('--> ')
    if valor == '1':
        nome = input('Entre com seu nome: ')
        comida = input('Entre com a comida preferida: ')
        dados = {
            'nome': nome,
            'comida': comida
        }
        crud.incluirDB(dados)
    elif valor == '2':
        chave = input('Qual o valor da chave: ')
        resultados = crud.lerDB(chave)
        for resultado in resultados:
            print(resultado.key())
            print(resultado.val())
    elif valor == '3':
        chave = input('Qual o valor da chave: ')
        nome = input('Entre com seu nome: ')
        comida = input('Entre com a comida preferida: ')
        dados = {
            'nome': nome,
            'comida': comida
        }
        crud.alterarDB(chave, dados)
    elif valor == '4':
        chave = input('Qual o valor da chave: ')
        crud.deleteDB(chave)
    else:
        break






