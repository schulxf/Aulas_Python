"""
Retorno de valores das funções (return)
"""

def soma(x,y):     ## a função é um liquidificador, os parametros são os ingredientes
    if x > 10:
        return [10, 20]
    return x + y   ## e o return é o item q sai depois de usar o liqui, a função deixa de ser valor None e passa a ter o valor do return

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11,55))