"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):    --- defino que a função soma deve receber os parametros x e y
#     print(x + y)   --- toda vez que eu executar a função soma, ele vai printar x + y

# soma (321,89745)   --- chamei a função soma onde x é 321 e y é 89745, logo ele vai executar a função
#                    --- realizando o que está dentro dela.   

def soma (x,y):
    print(f'{x =} + {y =} é igual a', x + y)

soma(589, 720)

soma(y=720, x=589)     ## pode inverter desde q seja informado dentro do parenteses
