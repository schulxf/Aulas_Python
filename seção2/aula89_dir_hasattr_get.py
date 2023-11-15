# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

# if hasattr(string, 'upper'):
#     print('Existe upper')
# para verificar se tem o atributo upper na variavel string fazemos esse I

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # get attribute (variavel, metodo)(), basicamente ficando getattr(string.upper())
else:
    print('Não existe o método', metodo)


# no modo debug se eu entrar no debug console e digitar dir(string) vai mostrar todas as opções de metódo pra variavel

