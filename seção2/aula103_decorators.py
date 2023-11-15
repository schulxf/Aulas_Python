# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criarfuncao(func):                   # criarfuncao recebe o parametro funcao, para q eu crie uma função usando variavel
    def interna(*args, **kwargs):        # para isso eu preciso ter uma função interna, essa recebe qualquer tipo de arg e kw
        for arg in args:                 # para cada arg no args, checa a função is_string, pra ver se é string
            is_string(arg)               # se não for, vai levantar a excessão que está dentro da função is_string
        return func(*args, **kwargs)     # aqui, dentro da interna, eu retorno a função que eu recebi atuando nos parametros
    return interna                       # e no escopo da primeira função eu retorno a interna já resolvida.

@criarfuncao
def inverte_string(string):             
    return string[::-1]

def is_string(param):                   # minha função recebe um parametro
    if not isinstance(param, str):      # se meu parametro não for str
        raise TypeError('param deve ser string.')                 # levanta um erro, nesse caso de tipo



# inverte_string_checando_param = criarfuncao(inverte_string)  ## def criarfuncao(inverte_string), só que meus param internos
#                                                              ## não foram definidos ainda

# invertida = inverte_string_checando_param('123') ## aqui é basicamente essa estrutura:

# def criarfuncao(inverte_string):                   
#     def interna('123'):        
#         for arg in args:               
#             is_string(arg)             
#         return inverte_string('123')     
#     return interna 



print(inverte_string('Flávio'))
