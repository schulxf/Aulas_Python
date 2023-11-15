# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]


# para cada item na lista, se item for int ou float, printa item, e printa item * 2
for item in lista: 
    if isinstance(item, (int, float)):
        print('INT e Float')
        print(item, item * 2)

    if isinstance(item, str):
        print('STR')
        print(item.upper())

        