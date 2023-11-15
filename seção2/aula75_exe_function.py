# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicacao(x):
#     return x * 2
# def triplicacao(x):
#     return x * 3
# def quadriplicacao(x):
#     return x * 4

# number1 = int(input('Digite um número para duplicar: '))
# number2 = int(input('Digite um número para triplicar: '))
# number3 = int(input('Digite um número para quadriplicar: '))

# print(duplicacao(number1))
# print(triplicacao(number2))
# print(quadriplicacao(number3))

def criar_multiplicador(multiplicador):     ## criei a função onde o argumento será o multiplicador
    def multiplicar(numero):                ## dentro da função criei outra função onde estara armazenado o numero para fazer a operação
        return numero * multiplicador       ## retorno para a função interior a operação 
    return multiplicar                      ## retorno para a função original a função interior já resolvida sem parentes 
#                                           ## para que esse valor possa ser inserido depois

duplicar = criar_multiplicador(2)           ## nesse caso estou criando a variavel duplicar onde a função já vem com o argumento (2)
#                                           ## ou seja, duplicar já está setado o argumento (2) do multiplicador nela
  
print(duplicar(10))                 ## a variavel duplicar já tem o multiplicador dentro dela, 
#                                   ## então dentro dos parentes entra o valor q desejo duplicar
#                                   ## que dentro da função não foi encerrado no return multiplicar, ficou pendente os parentes
#                                   ## então uso duplicar() com parenteses, para definir o numero dentro da função q estava pendente

triplicar = criar_multiplicador(3)
print(triplicar(53))

quadruplicar = criar_multiplicador(4)
print(quadruplicar(8495))