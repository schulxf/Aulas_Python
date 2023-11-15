lista = []

for x in range(3):
    for y in range(5):
        lista.append((x,y)) # como quero dois valores por indice tem que ser tupla


## LIST COMPREHENSION COM MAIS DE 1 FOR
lista_com_map = [
    (x, y) for x in range(3)
    for y in range (5)
]

## LIST COMPREHENSION DENTRO DE LIST COMPREHENSION
lista_com_comprehension = [
    [(x,letra) for letra in 'ABC']
    for x in range(3)
    
]

print(lista_com_comprehension)