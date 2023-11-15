"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None    ## flag sem valor

if condicao:
    passou_no_if = True ## flag com valor, se passar no if condicao, ela será exibida!
    print('Faça algo')
else:
    print('Não faça algo')


## nesse caso acima, o passou_no_if = None, não tem valor nenhum, mas dentro do if condicao foi setado
## que a variavel passou_no_if é True, então apenas dentro desse bloco if a variavel vai ser True, fora disso ela é None.

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')



## anotação de explicação:
## se a variavel foi criada dentro do bloco do if, o if precisa ser True pra que aquela variavel exista,
## se for False, ela nem vai ser criada.
## ex: if condicao: ##(condicao é False aqui)
##         passou_no_if: True
##         print(passou_no_if) 
## o print vai dar erro, pq a condicao é False, então o passou_no_if nem foi criado.