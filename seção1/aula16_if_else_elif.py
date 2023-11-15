# if  / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar ou "sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('c é tongo?')

# pra funcionar o if, elif e else, o print nesse caso tem que estar no bloco do if por exemplo
# só apertar tab que aparece 4 pontinhos e estará dentro do bloco
# caso 'entrada == 'entrar': seja true, ele pula os próximos códigos dos blocos e executa o próx. código fora do bloco

print('FORA DOS BLOCOS')