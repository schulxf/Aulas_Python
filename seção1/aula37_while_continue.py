"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue ### o continue ele para nele e volta pra repetição do while, ou seja, ele não imprime o 6 pq tá antes do print(contador)

    if contador >=10 and contador <=27 :
       # print('Não vou mostrar do 10 ao 27.')
        continue

    print(contador)

    if contador == 40:
        break



print('Acabou')
