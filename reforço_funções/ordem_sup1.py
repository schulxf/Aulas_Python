"""
Exercício 1: Função de Mapeamento
Crie uma função chamada mapeia(lista, funcao), onde lista é uma lista de números e funcao é uma função 
que recebe um número como argumento e retorna um número. A função mapeia deve aplicar a função dada a cada elemento 
da lista e retornar uma nova lista com os resultados.
"""

lista_sem_mapeamento = [1, 2, 3, 4, 5]

def mapeia(lista):
    resultado = []
    def multiplica (numero_multiplicador):
        for numero in lista:
            resultado.append(numero * numero_multiplicador)
        return resultado
    return multiplica

# mapeamento = mapeia(lista_sem_mapeamento)
print(mapeia(lista_sem_mapeamento)(2))


# então eu crio a função mapeia, eu defini que o mapeamento é simplesmente multiplicar por 2, então minha lista deve ser
# inteira multiplicada por 2.
# a função mapeia recebe como argumento a lista sem mapeamento.
# dentro dessa função eu crio outra função que se chama multiplica que recebe como parametro o valor, nesse caso o 2
# pra que eu possa ter essa lista com os números multiplicados eu preciso gerar uma nova lista, então eu crio
# a lista resultado = [], que está vazia, então eu posso adicionar cada multiplicação dentro dessa lista, ficando 
# do jeito que eu solicitei.
# dentro da função multiplica eu tenho que fazer a multiplicação por cada item da lista individualmente, então eu faço uma
# iteração com cada número. A cada número eu multiplico ele por 2 e adiciono na lista. Após terminar a iteração eu retorno
# o resultado atualizado e retorno a função multiplica. Pra poder usar as duas funções criadas eu tenho que criar uma váriavel
# pq só posso colocar um argumento por vez, então eu crio a variavel mapeamento, e dentro dela coloco a função
# mapeio e o argumento que é a lista, então fica assim - mapeamento = mapeio(lista_sem_mapeamento).
# se eu executar assim vai mostrar apenas que uma função por si só tem valor None, pq a função dentro dela não recebeu
# o valor do multiplicador. Então a minha variavel passa a ser a função mapeia já setada com a lista dentro.
# então eu posso usar a váriavel com parenteses, onde dentro do parenteses vai o valor da função multiplica, ficando assim:
# mapeamento(2) ou eu posso fazer sem criar variavel - mapeia(lista_sem_mapeamento)(2) - onde coloco os 2 argumentos
# em parenteses separados.