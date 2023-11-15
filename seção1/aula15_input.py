nome = input('Qual o seu nome? ')
peso = int(input('Qual o seu peso? '))
altura = float(input('Qual o seu tamanho? '))
imc = peso / (altura * altura)

# salvei as variaveis com input, o usuario determinou a variavel nome
# o input sempre vem em string, então para calculos usando input, tem que converter o formato
# peso = int(input('Qual o seu peso? '))
# nesse exemplo coloquei antes do input que deve converter para int


linha1 = f'O nome dele é {nome}, ele tem {altura} de altura,'
linha2 = f'pesa {peso}, e seu IMC é de {imc:.2f}'

print(linha1)
print(linha2)