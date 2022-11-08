'''
1. Calcule e exiba a área do círculo (A = pi*r2) de qualquer raio que
for digitado.
'''
# r = float(input("entre com o raio: "))
# pi = 3.1416
# A = pi*r**2
# print('A área é:', A)
'''
2. Calcule o volume do cilindro de raio 6 cm e altura 5 cm (V = pi*r2*h).
'''
# h = 5
# r = 6
# pi = 3.1416
# V = pi*r**2*h
# print('O volume é: ', V)
'''
3. Faça um procedimento que recebe a idade de um nadador por parâmetro
e retorna, também por parâmetro, a categoria desse nadador de
acordo com a tabela abaixo:
'''
from aula5_funcao import categoria

jose = categoria(20)
print(jose)
'''
4. Faça uma função que recebe um valor inteiro e verifica se o valor é
positivo ou negativo. A função deve retornar um valor booleano.
'''
def positivo_negativo(n):
    if n > 0:
        return True
    elif n < 0:
        return False
    else:
        return None

valores = [4, 6, 2, -8, 9, -12, 0]
for valor in valores:
    print(valor, positivo_negativo(valor))

'''
5. Faça uma função que recebe um valor inteiro e verifica se o valor é
par ou ímpar. A função deve retornar um valor booleano.'''

def par_impar(n):
    if n % 2 == 0:
        return True
    else:
        return False

for valor in valores:
    print(valor, par_impar(valor))

# valor = int(input('entre com um valor: '))
# print(par_impar(valor))

valores = []
while True:
    valor = input('entre com seu voto: ')
    if valor.lower() == 'sair':
        break
    valores.append(int(valor))

print(valores)
for valor in valores:
    print(valor, par_impar(valor))
 