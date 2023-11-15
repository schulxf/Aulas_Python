# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0


### QUESTION 1 --------------------------------------------
pergunta1 = perguntas[0]['Pergunta']
print(f'Pergunta: {pergunta1}')

for index, options in enumerate(perguntas[0]['Opções']):
    print(f' {index}) {options}')

first_choice = int(input('Digite uma das alternativas: '))
os.system('cls')
if first_choice == 2:
    print('Você acertou! Parabéns 🥳')
    acertos += 1
else:
    print('Você errou! ❌ ')

### QUESTION 2 --------------------------------------------
pergunta2 = perguntas[1]['Pergunta']
print(f'Pergunta: {pergunta2}')

for index, options in enumerate(perguntas[1]['Opções']):
    print(f' {index}) {options}')

second_choice = int(input('Digite uma das alternativas: '))
os.system('cls')
if second_choice == 0:
    print('Você acertou! Parabéns 🥳')
    acertos += 1
else:
    print('Você errou! ❌ ')


### QUESTION 3 --------------------------------------------
pergunta3 = perguntas[2]['Pergunta']
print(f'Pergunta: {pergunta3}')

for index, options in enumerate(perguntas[2]['Opções']):
    print(f' {index}) {options}')

third_choice = int(input('Digite uma das alternativas: '))
os.system('cls')
if third_choice == 1:
    print('Você acertou! Parabéns 🥳')
    acertos += 1
else:
    print('Você errou! ❌ ')

if acertos == 3:
    print('Você acertou todas! ✔️')
else:
    print(f'Você acertou {acertos} de 3!')

    


    

    