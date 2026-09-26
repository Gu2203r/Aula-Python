class Carro:

    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    def definir_motor(self, motor):
        self.motor = motor

    def definir_fabricante(self, fabricante):
        self.fabricante = fabricante

    def exibir_informacoes(self):
        print("\nNome:", self.nome, "\nMotor:", self.motor.nome, "\nFabricante:", self.fabricante.nome)

class Motor:

    def __init__(self, nome):
        self.nome = nome



class Fabricante:

    def __init__(self, nome):
        self.nome = nome

fabricante = Fabricante("Honda")
motor = Motor("V8")
carro = Carro("Civic")

carro.definir_fabricante(fabricante)
carro.definir_motor(motor)

carro.exibir_informacoes()


