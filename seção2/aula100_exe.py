# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy



novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1 , 2)}
# desempacota em uma nova lista, e pega a chave 'preco': pega o valor da chave e multiplica por 1.1


    for p in copy.deepcopy(produtos)
        

    ]

print(*novos_produtos, sep='\n')
    
print()

ordenados_preco = copy.deepcopy(sorted(novos_produtos, key= lambda item: item['preco']))

print(*ordenados_preco, sep='\n')

print()

ordenados_nome = copy.deepcopy(
    sorted(ordenados_preco, 
           key=lambda nome: nome['nome'] 
           ))

print(*ordenados_nome, sep='\n')

