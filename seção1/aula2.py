# \r\n -> CRLF, quebra de linha
# \n -> LF, quebra de linha do Linux
# Por padrão, a quebra de linha é automática
# Mas caso eu queira mudar é só usar o end=
# end='##\n' add a # e quebra linha com o /n 
print(123,456, sep=',', end='##\n') 
print(789,456, end='\n')