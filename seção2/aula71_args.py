"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):     ## define a função soma, sem limitar os parametros, empacotando
    total = 0        ## guarda a soma numa variavel
    for numero in args:  ## para cada numero no args
        total += numero  ## soma pra variavel "total" o número da iteração atual
    return total         ## depois de somar todas as iterações, retorna o valor da soma


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))           
# print(*numeros)