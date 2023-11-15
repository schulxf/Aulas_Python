## Calculadora com while

while True:

    prime_num = input('Digite o primeiro número: ')
    segu_num = input('Digite o segundo número: ')
    op_arit = input('Digite qual operação deseja fazer: ')


    numeros_validos = None

    try:
        num_1_float = float(prime_num)
        num_2_float = float(segu_num)
        numeros_validos = True
    except:
        numeros_validos = None


    if numeros_validos is None:
        print('Um ou ambos os números são inválidos')
        continue
    #print(numeros_validos) #flag

    op_permitidos = '+-*/'

    if op_arit not in op_permitidos:
        print('Operador inválido.')
        continue

    if len(op_arit) > 1:
        print('Digite apenas um operador!')

    soma = num_1_float + num_2_float
    subt = num_1_float - num_2_float
    multip = num_1_float * num_2_float
    divis = num_1_float / num_2_float

    if op_arit == '+' :
        print(soma)

    elif op_arit == '-' :
        print(subt)
    elif op_arit == '*' :
        print(multip)
    elif op_arit == '/' :
        print(divis)


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Você saiu do programa.')
        break
        







    ## não funcionou

    #first_int_num = int.prime_num
    # sec_int_num = int.segu_num

    # soma = (first_int_num + sec_int_num)
    # sub = (first_int_num - sec_int_num)
    # multi = (first_int_num * sec_int_num)
    # div = (first_int_num / sec_int_num)

    # #print(f'{prim_num} numa operação de {op_arit} com o {seg_num} é igual a ')

    # if op_arit == + :
    #     print(f'{first_int_num} numa operação de {op_arit} com o {sec_int_num} é igual a {soma} ')
    # elif op_arit == '-':
    #     print(f'{first_int_num} numa operação de {op_arit} com o {sec_int_num} é igual a {sub}')
    # elif op_arit == '*':
    #     print(f'{first_int_num} numa operação de {op_arit} com o {sec_int_num} é igual a {multi} ')
    # elif op_arit == '/':
    #     print(f'{first_int_num} numa operação de {op_arit} com o {sec_int_num} é igual a {div}')
