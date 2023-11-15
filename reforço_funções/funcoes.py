produtos = ['ABC123', 'abd012', 'ABS1111', 'AbB222']
texto = ' abd012 '
texto2 = 'O restante do código permanece praticamente o mesmo, que pode ser usada para fazer qualquer per'
## O texto tem tem espaços antes e depois e está tudo em minúsculo

## A função criar serve para tratar o texto, e o argumento solicitado será o texto que deve ser tratado
## Dentro da função consta o tratamento sendo .upper() para deixar maiúsculo e .strip() para remover espaços no inicio e no fim

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

## O return texto serve para devolver para a função o texto tratado, ou seja, passou por todos os códigos.

print(tratar_texto(texto2))

## Com o for, consigo tratar diretamente na lista os produtos

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto) ## aqui defino que a lista é igual ao produto já tratado
    

## vai imprimir a lista atualizada já tratada
print(produtos)