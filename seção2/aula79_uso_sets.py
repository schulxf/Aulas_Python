# Exemplo de uso dos sets

letra_armazenada = set()

while True:
    letra = input('Digite: ')
    letra_armazenada.add(letra.lower())

    if 'l' in letra_armazenada:
        print('Parabéns')
        break
    print(letra_armazenada)