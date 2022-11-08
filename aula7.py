# matriz = [
#     [1, 'A', 33],
#     [2, 'B', 22],
#     [3, 'J', 99],
#     [4, 'K', 55]
# ]
# for linha in matriz:
#     print(linha)

# for linha in range(len(matriz)):
#     print(matriz[linha])

# notas_alunos = [
#     [3, 5, 6],
#     [4, 2, 9],
#     [9, 7, 5],
#     [1, 1, 1]
# ]

# for notas in notas_alunos:
#     #print(notas)
#     for nota in notas:
#         print(nota)


# matriz = [
#     [3, 5, 6],
#     [4, 2, 9],
#     [9, 7, 5],
#     [1, 1, 1]
# ]
# soma = 0
# for linhas in matriz:
#     print(linhas)
#     soma_linha = 0
    
#     for coluna in linhas:
#         print(coluna)
#         soma_linha = soma_linha + coluna
#         soma = soma + coluna
#     print('soma linha: ', soma_linha)
# print('soma é: ', soma)

matriz = [
    ['andre', 3, 5, 6],
    ['joao', 4, 2, 9],
    ['pedro', 9, 7, 5],
    ['jose', 1, 1, 1]
]

for l in range(len(matriz)):
    soma = 0
    for c in range(1, len(matriz[l])):
        #print(matriz[l][c])
        soma = soma + matriz[l][c]
    print(f'o aluno {matriz[l][0]} tem a soma {soma}')

if l == []:
    pass
elif l!= []:
    pass
elif l!= []:
    pass
elif l!= []:
    pass
else:
    pass

print()
lst = [
    ['andre', 3, 5, 6],
    ['joao', 4, 2, 9],
    ['pedro', 9, 7, 5],
    ['jose', 1, 1, 1]
]
for i in range(len(lst)):
    for j in range(1, len(lst[i])):
        if lst[i][j] > 0:
            print(lst[i][j], lst[i][j] < 0)