forbbiden_char = '.' 

def tratamento_entrada(entrada):
    entrada = entrada.lower().strip()
    return entrada

def corrigir_listas(func, lista):
    lista_atualizada = []
    for i, adjetivo in enumerate(lista):
        if forbbiden_char not in adjetivo:
            lista_atualizada.append(func(adjetivo))
        
    return lista_atualizada


adjetivos = ['   ugly',
             'beautiful   ',
             '   awe.some   ',
             'stinky**  ',
             'intel.ligent',
             'handsome']

adjetivos_corrigidos = corrigir_listas(tratamento_entrada, adjetivos)

print(adjetivos_corrigidos)