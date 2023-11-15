class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        
    def acelerar(self):
        print(f'{self.modelo} está acelerando')

primeiro_carro = Carro('Urus', 'Lamborghini')
primeiro_carro.acelerar()

class Math:
    def __init__(self):
        pass

    def somar(self, a, b):
        resultado = a + b
        return print(resultado) 

calculo = Math()
calculo.somar(45,38)

