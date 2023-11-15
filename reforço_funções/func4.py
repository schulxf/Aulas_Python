def ao_quadrado(x):
    return x * x

def mapear_quadrados(func, lista):
    resultado = []
    for item in lista:
        resultado.append(func(item))
    return resultado


area2 = [100, 152, 78, 96, 280]

area_ao_quadrado = mapear_quadrados(ao_quadrado, area2)

print(area_ao_quadrado)