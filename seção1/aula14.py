a = 'AaAaA'
b = 'BbBbB'
c = 1.1
string = 'a={} b={} c={}'
formato = string.format(a, b, c)

# os brackets puxam os primeiros argumentos (a,b,c) do format na ordem para o print

formato = '1. vai puxar o primeiro bracket: {} 2. segundo bracket: {} 3. terceiro: {}'.format(a, b, c)
print(formato)

# posso alterar a ordem ao colocar o numero de ordem dentro do bracket, começando sempre pelo zero
# a = 0 , b = 1 e c = 2

formato2 = '1. vai puxar o segundo bracket: {1} 2. terceiro bracket: {2} 3. primeiro: {0}'.format(a, b, c)

print(formato2)

# posso nomear o parametro invés de deixar 0,1,2,3... no .format

formato3= '1. segundo bracket: {bola} 2. terceiro bracket: {name3} 3. primeiro: {cudecachorro}'.format(cudecachorro=a, bola=b, name3=c)
print(formato3)