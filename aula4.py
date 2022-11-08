def soma(a=0, b=1):
    return a + b

import math
def hipotenusa(a, b):
    h = math.sqrt(a**2 + b**2)
    return h

lst = [(3, 4), (8, 6), (9, 5), (7, 9)]

for c, d in lst:
  s = soma(b=c, a=d)
  print('soma', s)
  d = hipotenusa(c, d)
  print('hipotenusa', d)

# s = soma()
#print(s)
l = [soma(b=c, a=d) for c, d in lst]
print(l)

def verficador(valor):
    if valor >= 0:
        return True
    else:
        return False


# while True:
#     a = int(input("valor: "))
#     t = input('soma ou veriacao')
#     if t == 'v':
#         print(verficador(a))
#     else:
#         print(soma(a, a))
vogais = ['a','e','i','o','u']
a = 'andre'
if a[3] in vogais:
    print('vogais')
else:
    print('consoante')