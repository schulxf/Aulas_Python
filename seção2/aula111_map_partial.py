# map - para mapear dados
from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem= 1.1)
# com partial não precisa criar uma função interna pra conseguir colocar um parametro na variavel

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]

# com o map não preciso fazer list comprehension - mapeamento de lista

def change_product_price(product):
    return {
        **product, 'preco': aumentar_dez_porcento(product['preco'])
    }

novos_produtos = map(change_product_price, produtos) # faz o mapeamento usando minha função na lista q eu passei

print_iter(produtos)

print_iter(novos_produtos)


print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)