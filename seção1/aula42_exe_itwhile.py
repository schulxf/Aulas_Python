frase = 'aa eeeoooo'

## string.count() conta quantos caracteres dentro da string.

### se eu colocar dentro do .count() o que eu quero, ele mostra quantas vezes apareceu
# print(frase.count('Python')) vai mostrar quantas vezes a palavra apareceu.

i = 0
tamanho_frase = len(frase)

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''



while i < tamanho_frase:                         # enquanto o indice não chegar na qtd de letras da frase, ele não para o while
    letra_atual = frase[i]                       # frase [0], logo, pegando a primeira letra - "O"



    if letra_atual == ' ':                       # se a letra atual for o espaço ' '               --- if só vai ser executado quando for um espaço!
        i += 1                                   # adiciona +1 para o indice
        continue                                 # e com o continue ele volta para o inicio do while


    quantidade_atual = frase.count(letra_atual)   # vai mostrar quantas vezes a letra dentro do .count() apareceu.

    if qtd_apareceu_mais_vezes < quantidade_atual:  # quando a quantidade atual de vezes que a letra aparece for maior que a que apareceu mais vezes anteriormente ativa o if
                                                    # com o if ativado, ele seta um novo valor pras variaveis.
                                                    # por exemplo: qtd_apareceu mais vezes (0) < quantidade atual (10), então o if vai ser ativado
        qtd_apareceu_mais_vezes = quantidade_atual  # logo eu seto que os dois são iguais, então o qtd_apareceu_mais_vezes que antes era (0) agora é (10)



        letra_apareceu_mais_vezes = letra_atual     # letra_que_apareceu_mais_vezes tá setado como string vazia - '' -, como o if foi executado durante uma letra
                                                    # e essa letra tinha a quantidade atual maior que a anterior, ele tira o valor vazio da variavel e torna a ser
                                                    # a letra atual

    
                       
    i += 1                                       # antes de voltar o loop, adiciona +1 no indice para que ele consiga em algum momento
                                                      # no tamanho de caracteres da frase, pq se não ele não para - loop infinito.

print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '   # a variavel foi setada dentro quando o ultimo if foi executado, logo ira mostrar a letra que apareceu + vezes
      f'{qtd_apareceu_mais_vezes}x '                # a variavel foi setada dentro quando o ultimo if foi executado, logo ira mostrar qnts vezes ela apareceu.
      )              
