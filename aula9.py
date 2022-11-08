'''
    1. Classe Bola: Crie uma classe que modele uma bola:
        a. Atributos: Cor, circunferência, material
        b. Métodos: trocaCor e mostraCor
'''
class Bola:
    def __init__(self, cor) -> None:
        self.__cor = cor
        self.circunferencia = 0.0
        self.material = 'couro'

    def trocaCor(self, p_cor):
        self.cor = p_cor

    def mostrarCor(self):
        print(self.__cor)

    def retornarCor(self):
        return self.__cor

bola = Bola('amarelo')
print(bola.circunferencia)
#print(bola.__cor)

#bola.trocaCor('azul')
bola.__cor = 'preto'
bola.mostrarCor()
print(bola.retornarCor())
'''
    2. Classe Quadrado: Crie uma classe que modele um quadrado:
        a. Atributos: Tamanho do lado
        b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    3. Classe Retangulo: Crie uma classe que modele um retangulo:
        a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
        b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
        c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
    4. Classe Pessoa: Crie uma classe que modele uma pessoa:
        a. Atributos: nome, idade, peso e altura
        b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
    5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
    6. Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
    7. Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
        a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
    8. Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
    9. Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
        a. Possua uma classe chamada Ponto, com os atributos x e y.
        b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
        c. Possua uma função para imprimir os valores da classe Ponto
        d. Possua uma função para encontrar o centro de um Retângulo.
        e. Você deve criar alguns objetos da classe Retangulo.
        f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
        g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
        h. O valor do centro do objeto deve ser mostrado na tela
'''