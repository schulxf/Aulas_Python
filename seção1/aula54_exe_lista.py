'''
Faça uma lista de comprar com listas;
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com
erros de índices inexistentes na lista
'''


# inserir = lista.append()
# apagar = lista.pop(indice)
# listar = print(indice, item)

# lista = []

# while True:
#     opcao = input(str('Selecione uma opção ou digite sair para fechar o programa: \n [i]nserir - [a]pagar - [l]istar: ' ))

#     if opcao == 'i':
#         opcao_i = input('O que deseja inserir na lista? ')
#         lista.append(opcao_i)   
#     elif opcao == 'a':
#         for indice, item in enumerate(lista):
#             indice = input('Qual excluir? ')
#             indice_int = int(indice)
#             item_removido = [indice_int]
#             lista.pop(indice_int)
#             print(f'O item foi excluído com sucesso!')
#             break
#     elif opcao == 'l':
#         for indice, item in enumerate(lista):
#             print(indice, item)
#     elif opcao == 'sair':
#         print('Programa encerrado com sucesso!')
#         break
#     else:
#         print('Opção Inválida!')


## solução do professor
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')







