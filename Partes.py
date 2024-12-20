# Parte 1
class Animal:
    def mover(self):
        pass

class Veiculo:
    def mover(self):
        pass

animal = Animal()
veiculo = Veiculo()
animal.mover()
veiculo.mover()

# Parte 2
class Cachorro:
    def falar(self):
        print("Au au!")

class Gato:
    def falar(self):
        print("Miau!")

cachorro = Cachorro()
gato = Gato()
cachorro.falar()
gato.falar()

class Papagaio:
    def falar(self):
        print("Olá!")

papagaio = Papagaio()
papagaio.falar()

# Parte 3
def chamar_fala(objeto):
    if hasattr(objeto, 'falar'):
        objeto.falar()
    else:
        print("Objeto não tem o método falar.")

chamar_fala(cachorro)
chamar_fala(gato)
chamar_fala(papagaio)

class Carro:
    pass

carro = Carro()
chamar_fala(carro)

# Parte 4
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

class Papagaio(Animal):
    def falar(self):
        print("Olá!")

class Peixe(Animal):
    def falar(self):
        print("Peixes não falam")

animais = [Cachorro(), Gato(), Papagaio(), Peixe()]
for animal in animais:
    animal.falar()

# Parte 5
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

retangulo = Retangulo(5, 10)
circulo = Circulo(7)
print(retangulo.area())
print(circulo.area())

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

triangulo = Triangulo(6, 8)
print(triangulo.area())

# Parte 6
class Calculadora:
    def somar(self, a, b, c=0):
        return a + b + c

calc = Calculadora()
print(calc.somar(2, 3))
print(calc.somar(2, 3, 4))

# Parte 7
class Forma:
    def desenhar(self):
        print("Desenhando uma forma")

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo")

class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado")

circulo = Circulo()
quadrado = Quadrado()
circulo.desenhar()
quadrado.desenhar()

# Parte 8
objetos = [Cachorro(), Gato(), Papagaio(), Peixe()]
for obj in objetos:
    if hasattr(obj, 'falar'):
        obj.falar()

objetos.append(Carro())
for obj in objetos:
    if hasattr(obj, 'falar'):
        obj.falar()

# Parte 9
class Pagamento:
    def processar_pagamento(self):
        pass

class Credito(Pagamento):
    def processar_pagamento(self):
        print("Pagamento por crédito processado.")

class Debito(Pagamento):
    def processar_pagamento(self):
        print("Pagamento por débito processado.")

class Pix(Pagamento):
    def processar_pagamento(self):
        print("Pagamento por Pix processado.")

pagamentos = [Credito(), Debito(), Pix()]
for pagamento in pagamentos:
    pagamento.processar_pagamento()

# Parte 10
class Transporte:
    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Transporte):
    def acelerar(self):
        print("Carro acelerando.")

    def frear(self):
        print("Carro freando.")

class Bicicleta(Transporte):
    def acelerar(self):
        print("Bicicleta acelerando.")

    def frear(self):
        print("Bicicleta freando.")

class Trem(Transporte):
    def acelerar(self):
        print("Trem acelerando.")

    def frear(self):
        print("Trem freando.")

class Aviao(Transporte):
    def acelerar(self):
        print("Avião acelerando.")

    def frear(self):
        print("Avião freando.")

def executar_transporte(transporte):
    transporte.acelerar()
    transporte.frear()

transportes = [Carro(), Bicicleta(), Trem(), Aviao()]
for transporte in transportes:
    executar_transporte(transporte)
