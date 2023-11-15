# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
# (1+1) ** (5+5) = 1024

print(conta_1)

# Precedência entre os operadores aritméticos define qual vai ser executado antes, igual na matemática normal.
#ex: multiplicação antes de adição ou subtração

conta_2 = 1 + 1 ** 5 + 5
# primeiro vai exponeciar 1 elevado ao 5, que dá 1
# depois vai somar 1 + 1 + 5 que dá 7
print(conta_2)