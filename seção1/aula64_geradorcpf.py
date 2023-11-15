"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  1   0  2  3  1  2  1  6  9
   10  0 16 21 6 10 4 18 18

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import random

# cpf = input('Digite seu CPF: ')


cpf_nove_dig = ''
for i in range(9):
    cpf_nove_dig += str(random.randint(0,9))


print(f'Nove primeiros digitos: {cpf_nove_dig}')

multiplicador_regressivo = 10
soma = 0

for numero in cpf_nove_dig:   ## para cada numero no cpf_nove_dig
    multiplicacao_realizada = int(numero) * multiplicador_regressivo
    soma += multiplicacao_realizada
    multiplicador_regressivo -= 1
    
print(f'Soma das multiplicações: {soma}')

resultado_resto_1 = (soma * 10) % 11


# primeiro_digito = True se o resultado_resto for igual ou menor que 9, se for False é 0
primeiro_digito = resultado_resto_1 if resultado_resto_1 <= 9 else 0 

print(f'O primeiro digito é {primeiro_digito}')

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
"""

cpf_dez_dig = cpf_nove_dig + str(resultado_resto_1)

print(f'Dez primeiros digitos: {cpf_dez_dig}')

multiplicador_regressivo_2 = 11
soma_2 = 0
for numero in cpf_dez_dig:
    multiplicacao_realizada = int(numero) * multiplicador_regressivo_2
    soma_2 += multiplicacao_realizada
    multiplicador_regressivo_2 -= 1
    
print(f'Soma das multiplicações: {soma_2}')

resultado_resto_2 = (soma_2 * 10) % 11


# segundo_digito = True se o resultado_resto for igual ou menor que 9, se for False é 0
segundo_digito = resultado_resto_2 if resultado_resto_2 <= 9 else 0 

print(f'O segundo digito é {segundo_digito}')

novo_cpf = f'{cpf_nove_dig}{primeiro_digito}{segundo_digito}'


print(f'Esse é o novo CPF {novo_cpf}')