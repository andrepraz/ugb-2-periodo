from crud import MyCrud

my_crud = MyCrud('cliente.sqlite')
my_crud.criar_tabela()

# results = my_crud.selecionar()
# print('RESULTADO:', results)
# for i in results:
#     print(i)

nome = input('Entre com o nome: ')
cpf = input('Entre com o cpf: ')

dados = {
    'tabela': 'clientes',
    'campos': ['nome', 'cpf'],
    'valores': [nome, cpf]
}

my_crud.inserir(dados)

# my_crud.alterar(a_id=2, a_nome='jose', a_cpf='223355446-56')
# results = my_crud.selecionar()
# print('RESULTADO:', results)
# my_crud.deletar(3)
# results = my_crud.selecionar()
# print('RESULTADO:', results)

my_crud.fecharDB()