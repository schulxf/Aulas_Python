# Exercício - Adiando execução de funções


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)



# multiplica_por_dez = criar_funcao(multiplica, 10)

def soma_cinco(x):
    def numero(y):
        return x + y
    return numero

soma_com_cinco = criar_funcao(soma_cinco, 5)
print(soma_com_cinco(10))
    
