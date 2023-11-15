## Crie funções onde caso o nome tenha mais de 4 caracteres, ele seja substituido por um "-"

def tamanho_maximo(palavra):
    qtd_permitida = 4
    if len(palavra) > qtd_permitida:
        return 'blocked'
    return palavra

def verificar_palavra_curta(func, lista):
    result = []
    for item in lista:
        result.append(func(item))
    return result

nomes = ['Flávio',
         'João',
         'Dory',
         'Janine',
         'Wave',
         'Cláudio',
         'BRTT']

nomes_qtd_max = verificar_palavra_curta(tamanho_maximo, nomes)
print(nomes_qtd_max)