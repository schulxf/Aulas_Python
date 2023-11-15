# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa1 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa.values()
# print(a,b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa2 = {
    'nome': 'Rogério',
    'sobrenome': 'Alves'
}

dados_pessoa = {
    'idade':'28',
    'altura':'1.8'
}

pessoas_completa = {**pessoa2, **dados_pessoa, 'carro': 'Hilux'}

print(pessoas_completa)

# args e kwargs
# args é os argumentos não nomeados, exemplo:
# def argumentos_não_nomeados (1, 2, 'a')
# e keyword args são os nomeados, exemplo:
# def kwargs(nome='Jão', idade='38')


## ----------- EMPACOTAMENTO DOS DICIONÁRIOS
def mostro_argumetnos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumetnos_nomeados('abc', 485123, nome='Joana', qlq=123)

## ------------ DESEMPACOTAMENTO DOS DICIONÁRIOS

mostro_argumetnos_nomeados(**pessoas_completa)