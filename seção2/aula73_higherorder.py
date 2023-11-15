"""
Higher Order Functions
Funções de primeira classe
"""


# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'

# def executa(funcao, *args):
#     return funcao(*args)


# print( 
#     executa(saudacao, 'Bom dia', 'Flávio'))

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()

def hello(function):
    text = function('Hello')
    print(text)

hello(loud)
hello(quiet)




def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))
