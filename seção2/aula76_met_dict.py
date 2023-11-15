# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Flávio',
    'sobrenome': 'Schulz',
    'lista1': [0, 1, 2],
}


## ---------- pode converter pra lista pra facilitar a visualização ---------- #

print(len(pessoa))     ## imprime quantidade de chaves

print(list(pessoa.keys()))   ## imprime as chaves do dicionario

print(pessoa.values()) ## imprime os valores do dicionario

print(pessoa.items())  ## imprime as chaves e os valores, posso iterar com for e separar chave e valor

for chave, valor in pessoa.items():
    print(chave, valor)

print(pessoa.get('nome')) ## pega o valor de uma chave especifica, posso por depois da virgula no argumento um valor default, geralmente None

# nome = pessoa.pop('nome')  ## apaga do dicionario a chave e valor 
# print(nome)                ## se eu quiser saber o nome apagado ainda consigo
# print(pessoa)              ## agora q foi excluido, se eu imprimir a lista não vai constar

# ultima_chave = pessoa.popitem()    ## apaga do dicionario a ultima chave e valor 
# print(ultima_chave)                ## se eu quiser saber o valor apagado ainda consigo
# print(pessoa)              ## agora q foi excluido, se eu imprimir a lista não vai constar

pessoa.update({           ### pode adicionar, atualizar no dictionary
    'nome': 'Rogislei',   ## posso também criar uma tupla ou lista de variavel e fazer pessoa.update(tupla)
    'idade': 37
})





pessoa.setdefault('idade', 0) ## como não existe a chave idade na lista, seta como padrão o valor zero caso seja solicitado

## --------------------- shallow copy ------------------------- ##
# copia a lista, se eu setasse pessoa2 = pessoa1, qualquer alteração que eu fizesse na pessoa2 iria refletir na pessoa1
# por que seria pessoa = pessoa2, ou seja, a mesma coisa, e com a cópia não tem esse problema
# mas caso tenha um objeto mutavel dentro por exemplo uma lista, ele vai se referir à mesma lista na memória, então as duas
# vão sofrer alteração

pessoa2 = pessoa.copy()

pessoa2['nome'] = 'Janine'

pessoa2['lista1'][0] = 99999 ## exemplo do shallow copy, onde alterei do pessoa2, mas mudou também do pessoa1

print(pessoa)
print(pessoa2)

## --------------------- deep copy ------------------------- ##
# precisa importar o módulo copy, e utilizar copy.deepcopy(pessoa) por exemplo
# para não ter o problema do shallow copy, mas por conta de processamento pode não ser muito bom
# dependendo do tamanho do dicionário
# no shallow copy, alterar o pessoa 2, alterou o pessoa1
# mas no deep copy, só alterou o pessoa 3 e não mexeu no pessoa2 e pessoa1

import copy

pessoa3 = copy.deepcopy(pessoa)

pessoa3['lista1'][0] = 55555101010

print(pessoa3)