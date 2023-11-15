import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Jairo', 43)
p3 = Pessoa('Jooã', 37)

database = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(database, arquivo, ensure_ascii=False, indent=2)
