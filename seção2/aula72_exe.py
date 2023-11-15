# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.



def multi(*args):
    total = 1   ## pra resolver o problema de ter que fazer o numero vezes o proximo numero, é só colocar pra multi por 1 o primeiro numero
    for numero in args:
        total *= numero         
    return total

multiplication = multi(10,2, 3, 4, 5)

print(multiplication)

print(10*2*3*4*5)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def even_or_odd(x):
    if x % 2 == 0:
        return True
    return False
    
number = input('Type a number: ')
x = int(number)

if even_or_odd(x) is True:
    print('Your number is even!')
else:
    print('Your number is odd!')

