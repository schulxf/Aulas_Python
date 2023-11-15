# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'tenho','__iter__']
iterator = iter(iterable)  ## no iter() tem dentro dele __iter__ e __next__ já fazendo sozinho o processo


# iterator = (next(iterable))
# única responsabilidade do iterator é entregar o próximo valor, não sabe o anterior, o ultimo, o primeiro...


# Generator - funções que sabem pausar em determinado momento
# Todo generator é um iterator, mas um iterator não é um generator
# No generator pode user if for função...
# É UMA FUNÇÃO QUE PAUSA!

# ao fazer o list comprehension assim, todos esses números ficam salvos na memória, pode ficar pesado
# generator = [n for n in range(10000)]

# com o generator invés de eu usar [] eu uso (), ele não salva todos os valores na memória, entrega um por vez
generator = (n for n in range(10000))


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator: invés de salvar todos os numeros ele vai dando next até terminar
#     print(n)


# vantagem da lista: como está na memória posso acessar por indice qualquer valor dela
# generator não tem indice, tamanho, len