produtos = [1, 2, 3, 4, 5, 10, 100, 2500]


def dobrar(numero):
    return numero * 2

def aplicar_funcao(funcao, lista):        # a função aceita como argumento a função dobrar e a lista
    resultado = []                        # como queremos dobrar a lista, precisamos criar uma lista do zero e ir adicionando os valores att
    for item in lista:                    # para cada item na lista produtos vamos iterar adicionando a funcao dobrar ao item
        resultado.append(funcao(item))    # aqui adiciona a lista resultado que estava vazia o item já dobrado de valor, pq colocamos a função dobrar
    return resultado                      # retorna a lista atualizada

resultado = aplicar_funcao(dobrar, produtos) # aqui é somente a execução da função, onde defino qual será a função utilizada e a lista
#                                            # que nesse caso a função é a função dobrar, que criei acima, e a lista produtos
print(resultado)