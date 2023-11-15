class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Flávio', 'Schulz')

p2 = Pessoa('Janine', 'Anjos')

print(p1.nome)
print(p2.nome)
        