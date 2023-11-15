class Pessoa:
    
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome        
        self.idade = idade 

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Flávio', 25)
p2 = Pessoa('Janine', 24)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.__dict__)
print(vars(p1))
p1.nome = 'auiefhasd'

print(p1.nome)

p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)

del p1.__dict__['outra']
print(p1.__dict__)
