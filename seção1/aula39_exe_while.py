"""
Iterando strings com while

"""
#       0123456789....
nome = "Flávio Augusto" ## iterável = que pode ser alterado

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)


indice = 0

while indice < len(nome):
    aspas = '*'
    print(aspas + nome[indice] + aspas)
    indice += 1
    

## versão do prof


# nome = 'Maria Helena'

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)