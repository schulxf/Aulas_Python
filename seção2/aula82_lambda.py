# Pra criar uma função eu preciso colocar os parametros nela, os parametros colocados nessa função aqui são pra 
# poder executar uma função dentro de outra função. Eu passei dois argumentos pra ela, primeiro o argumento função que
# como o nome diz será uma função, e passei *args, que pode ser quantos argumentos eu quiser depois. Por exemplo:
# def executa(somar, 10, 20, 30, 40). O return dentro da função executa é pra fazer com que a função colocada dentro
# do parametro, nesse caso somar, retorne a função somar com os parametros que foram colocados no def executa().
# a função somar é definida em outro lugar, mas na teoria ficaria assim:
# def executa(função de somar, 10,20,30,40)
#   return função de somar(10,20,30,40)

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


# Com a lambda, posso criar funções em 1 linha só, sem precisar fazer def funcao(). Vou criar agora a função
# soma usando lambda, daí posso colocar na função executa criada lá em cima pra fazer a mesma coisa, mas com menos código.
# então coloco a função executa, e dentro dela coloco lambda (def) e os parametros (x,y): - depois dos dois pontos (:)
# é só colocar o que eu quero que a função faça, então x+y, que já retorna automático, não precisa usar return
# só que como na função soma criada antes precisa colocar os parametros pra fazer a soma, aqui também
# precisa colocar os parametros reais que vão ser executados, então só coloca uma vírgula e coloca os valores, que ficaria
# lambda x,y: x + y, 2, 3 - que fica exatamente a mesma coisa que soma(2,3)

print(
    executa(
        lambda x,y: x + y,
        2, 3
    )
)



# --------------------------------------------------------------------------
# Função de Ordem Superior: cria_multiplicador é uma função que retorna outra função.
# Neste exemplo, ela cria uma função de multiplicação baseada no 'multiplicador' fornecido.
# def cria_multiplicador(multiplicador):
#     # Função interna 'multiplica' que multiplica um número pelo 'multiplicador' fornecido.
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# # Exemplo de uso: cria uma função que multiplica números por 2 e a aplica ao número 5.
# multiplica_por_2 = cria_multiplicador(2)
# resultado = multiplica_por_2(5)  # O resultado será 10 (5 * 2).

duplica = executa(
    lambda m: lambda n: n * m, 
    2
)
print(duplica(30))

print(executa(
    lambda *args: sum(args), ## def (argumentos): soma(argumentos)
    1,2,3,4,5,6,7,8
))