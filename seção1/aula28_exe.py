"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
int_idade = int(idade)
ano = int(2023)

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome não contém espaço')
    print('Seu nome tem', len(nome), 'caracteres.')
    print('A primeira letra do seu nome é', (nome[0]))
    print('A última letra do seu nome é', (nome[5]))
    print(f'Sua idade é', idade)
    print(f'Você nasceu aproximadamente no ano de', ano - int_idade)
else:
    print('Você deixou campos vazios!')

