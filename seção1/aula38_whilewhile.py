qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:

    coluna = 1
                                        ### while dentro de while executa o que tá mais dentro do bloco até
                                        ### terminar, daí repete o mais distante
                                        ### executa o programa pra entender melhor ou usa o debug!
   
    while coluna <= qtd_colunas:
         
        print(f'{linha=}, {coluna=}')   ### colocando f'{string=}' dá pra visualizar melhor o que é linha e coluna

        coluna += 1

    linha += 1

print('Acabou')