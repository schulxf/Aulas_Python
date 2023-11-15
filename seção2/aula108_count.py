from itertools import count

c1 = count(1, 2)  # count só pode ter inicio, não tem fim, mas tem pula de tanto em tanto (step)
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

print()
print('count')

for i in c1:
    if i > 10:
        break

    print(i)

print()

r1 = range(1, 10, 2) # inicio, fim, pula de tantos em tantos

print('range')
for i in r1:
    print(i)