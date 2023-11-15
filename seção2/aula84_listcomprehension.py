
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

# ---------- MAPEAMENTO DE DADOS EM LIST COMPREHENSION
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  ## novo dicionario onde altera o preço dos produtos 5% a mais
    if produto['preco'] > 20 else {**produto}      ## só altera SE preço do produto for maior que 20, caso não, valor original

    for produto in produtos
]

# p(novos_produtos)


## -------- FILTRO DE DADOS EM LIST COMPREHENSION

lista2 = [n for n in range(11) if n < 5] # criando uma lista: um numero para cada numero no range(11), SE o numero for < 5

p(lista2)


# essa variavel é uma nova lista com o mapeamento dos dados, onde aumenta 5% do valor se for mais que 20
novos_produtos_com_filtro = [
    {**produto, 'preco': produto['preco'] * 1.05}  
    if produto['preco'] > 20 else {**produto}      

    for produto in produtos

    if produto['preco'] >= 20 and produto['preco'] * 1.05 > 10 
    # filtros devem ser adicionados depois do for, nesse caso ele filtra se o valor é maior que 10
]

p(novos_produtos_com_filtro)