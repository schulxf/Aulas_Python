# try, except, else and finally

try:
    print('Abriu o Arquivo')
    8/0
except ZeroDivisionError:
    print('Deu erro no arquivo!')
    
else:
    print('Não deu erro')

finally: ## sempre será executado
    print('Fechou o arquivo')