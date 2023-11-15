"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')


if entrada.isdigit():  ### isdigit verifica se a entrada é apenas numeros, logo float não funciona por conta do ponto (.)
    num_int = int(entrada)            ## se a entrada é apenas número, cria uma variavel convertendo a entrada para inteiro
    if (num_int % 2 ==0):              ## se o numero inteiro não tem resto na divisão, ele é par
        print('É um número par.')
    else:
        print('É um número impar.')
else:
    print('Você não digitou um número inteiro!')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_input = input('Qual a hora? ')
hora_int = int(hora_input)


if hora_int >= 0 and hora_int <= 11 :
    print('Bom dia!')
elif hora_int >= 12 and hora_int <= 17 :
    print('Boa tarde!')
elif hora_int >= 18 and hora_int <= 23 :
    print('Boa noite!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_input = input('Qual o seu nome? ')
tamanho_nome = len(nome_input)
nome_int = int(tamanho_nome)

if nome_int <= 4:
    print('Seu nome é pequeno...')
elif nome_int == 5 or nome_int == 6 :
    print('Seu nome é normal.')
elif nome_int > 6 :
    print('Seu nome é grande!')    



