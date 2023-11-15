# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}
# Jeito sem Dict Comprehension
for chave, valor in produto.items(): 
    print(chave, valor)

# Com Dict Comprehension
dc_em_uma_linha = {
    chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items()
}

dc_melhor_leitura = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

## listas que tem os valores parecidos com {chave: valor} podem ser convertidas para dict *******************


## Set Comprehension

s1 = {2 ** i for i in range(10)}

