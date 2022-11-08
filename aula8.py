# lista = []
# while True:
#     produto = input('Entre com produto: ')
#     if produto.upper() == 'SAIR':
#         break
#     quantidade = int(input('Entre com a quantidade: '))
#     preço = float(input('Entre com o preço: '))
#     registro = (produto, quantidade, preço)
#     lista.append(registro)

# print(lista)
# lista = [
#     ('maçã', 5, 10.0),
#     ('banana', 3, 12.0),
#     ('figo', 9, 16.0)
# ]
# faturamento = 0
# for i in lista:
# #     print(i[0], i[1] * i[2])
# #     faturamento = faturamento + (i[1] * i[2])
# # print(faturamento)

# def somaLimpo(l):
#     soma = []
#     for i in l:
#         soma.append(0)
#     return soma

# def contaMatriz(m, s, lista, mensagem):
#     linha = len(m)
#     coluna = len(m[0])
#     for l in range(linha):
#         for c in range(coluna):
#             s[m[l][c]] = s[m[l][c]] + 1
#     for i in range(len(lista)):
#         print(lista[i], 'com', s[i], mensagem)


# matriz = [
#     [1,3,2,5,2,0],
#     [3,4,1,2,1,4],
#     [5,1,2,5,3,5],
#     [4,2,4,3,4,1],
#     [2,5,3,2,2,5],
#     [0,0,0,0,0,0],
#     [3,4,1,5,3,2],
#     [2,3,2,2,5,1],
#     [1,4,4,4,3,1],
#     [0,1,5,1,5,2],
#     [2,5,2,3,2,5],
#     [3,3,3,3,3,3]
# ]

# bichos = ['vazio','porco','vaca','cachorro','gato','galo']
# contagem = [0,0,0,0,0,0]
# # somatorio = somaLimpo(bichos)
# # contaMatriz(matriz,somatorio,bichos, 'prêmio')

# for i in matriz:
#     print(i)
#     for j in i:
#         print(j)
#         contagem[j] = contagem[j] + 1
# print('contagem', contagem)

class Copo:
    def __init__(self, cor, altura, material):
        self.cor = cor
        self.altura = altura
        self.material = material

copo_plastico = Copo('branco', 7.5, 'plástico')
copo_metal = Copo('cinza', 8, 'alumínio')
print(copo_plastico.altura)
copo_plastico.altura = 7.5
print(copo_metal.altura)
print(copo_plastico.altura)
print(copo_metal.material)
print(copo_plastico.material)