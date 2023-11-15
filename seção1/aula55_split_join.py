"""
split e join list e str
split - divide uma string - .split() - se vazio separa por espaço vazio, oq estiver dentro vai determinar onde vai separar gerando uma lista
join - une uma string
strip - corta espaços vazios no inicio e no fim
rstrip - corta espaço vazio da direita e lstrip - corta espaço vazio da esquerda
"""

frase = '   Olha só que   ,    coisa interessante   '
lista_frases_crua = frase.split(',')                ## aqui estou separando a frase pela ',' ficando cheio de espaços vazios

lista_frases = []                                   ## aqui estou setando a variavel lista_frases que quero q seja corrigida dos espaços
for i, frase in enumerate(lista_frases_crua):       ## aqui com o loop, estou pegando o indice e a frase do enumerate(lista_frases_crua)
    lista_frases.append(lista_frases_crua[i].strip()## aqui estou adicionando ao corrigido a frase crua no indice correto mas sem espaços .strip()
                        )
    
frases_unidas = '-'.join(lista_frases)              ## join une os iteraveis com a string coloca no inicio

print(lista_frases)

print(lista_frases_crua)

print(frases_unidas)