nome = 'Flávio Augusto de Castro Schulz Jr.'
altura = 1.77
peso = 95
imc = (peso / (altura * altura))



#print(nome, 'tem', altura, 'de altura,')
#print('pesa', peso, 'e seu IMC é de ', imc)

#linha_1 = 'nome tem altura de altura'
# inserir o f antes possibilita variaveis dentro da string
linha_1 = f'{nome} tem {altura:.2f} de altura'
#o que fica dentro do bracket é a variavel
# {altura:.2f} = o :.2f é a formatação para duas casas decimais, se for :.3f será 3 casas decimais
print(linha_1)

linha_2 = f'pesa {peso} quilos e seu IMC é de {imc:.2f}'
print(linha_2)

