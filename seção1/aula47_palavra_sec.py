"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_escolhida = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:                         
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_escolhida:           # se letra_digitada estiver no palavra_escolhida
        letras_acertadas += letra_digitada          # letras_acertadas guarda a letra_digitada

    palavra_formada = ''                            # usado para guardas as tentativas que ocorrem dentro do for
    for letra_secreta in palavra_escolhida:           # configura a variavel letra_secreta na palavra_escolhida
        if letra_secreta in letras_acertadas:          # se letra_secreta está nas letras_acertadas
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'                      ## como é repetição, ele vai checar se a letra_secreta está nas letras_acertadas
                                                        ## se não estiver ele vai printar um asterisco no lugar!
    print(palavra_formada)
    if palavra_formada == palavra_escolhida:
        os.system('cls')
        print(f'Você Ganhou em {numero_tentativas} tentativas!')
        letras_acertadas = ''
        numero_tentativas = 0
    














""" VERSÃO CHATGPT
palavra_secreta = 'xarope'
tentativas = 0
max_tentativas = 6  # Defina aqui o número máximo de tentativas que o usuário tem

# Crie uma lista para armazenar as letras adivinhadas
letras_adivinhadas = ['*'] * len(palavra_secreta)

while '*' in letras_adivinhadas and tentativas < max_tentativas:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) == 1 and letra_digitada.isalpha():  # Verifica se foi digitada apenas uma letra
        if letra_digitada in palavra_secreta:
            # Atualiza a lista de letras adivinhadas com a letra correta
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra_digitada:
                    letras_adivinhadas[i] = letra_digitada
            print(''.join(letras_adivinhadas))  # Mostra o progresso
        else:
            print('*' * len(palavra_secreta))  # Mostra a palavra com letras escondidas
            print('Letra não encontrada na palavra secreta.')
            tentativas += 1
    else:
        print('Por favor, digite apenas uma letra válida.')

if '*' not in letras_adivinhadas:
    print('Parabéns, você adivinhou a palavra secreta!')
else:
    print('Game over! A palavra secreta era:', palavra_secreta)

"""