# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
# o return para e acaba ali, o generator pausa e volta


def generator(n=0):
    yield 1 # pausar
    print('Continuando')
    print('Continuando2')

    yield 2 # Pause
    print('Mais um')

    yield 3 # Pause
    print('Vou terminar')

gen = generator(n=0)

print(next(gen))
print(next(gen))
# como só coloquei next 2 vezes, ele pausou no segundo valor e não deu o terceiro yield



# entrou dentro da função e pausou no yield, com o next(gen) ele vai me o valor
# funciona igual o debug, ele tá na linha, mas só depois que passo pra próxima linha que ele entrega o valor
# por isso tem q usar o next


def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        
gen2 = generator2(n=95, maximum=100)
for n in gen2:
    print(n)

    