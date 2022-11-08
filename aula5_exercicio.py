# notas = []
# while True:
#     c = input('Quer cadastrar s/n: ')
#     if c == 's':
#         nome = input("entre com seu nome: ")
#         nota_1 = input('entre com a nota 1: ')
#         nota_2 = input('entre com a nota 2: ')
#         notas.append((nome, nota_1, nota_2))
#     else:
#         break
notas = [
    ('andre', 10, 9),
    ('joao', 9, 6),
    ('pedro', 6, 7)
]

# notas_dic = [
#     {'nome': 'andre', 'nota1':10, 'nota2':9},
#     {'nome': 'joao', 'nota1':9, 'nota2':6},
#     {'nome': 'pedro', 'nota1':6, 'nota2':7},
# ]
# for nota in notas_dic:
#     print(nota['nome'])


print(notas)

for nota in notas:
    # print(nota[1], nota[2])
    media = (nota[1] + nota[2])/2
    if media >= 7:
        print(f'o aluno {nota[0]} teve media {media} ele foi aprovado')
    else:
        print(f'o aluno {nota[0]} teve media {media} ele foi reprovado')