from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key=lambda nota: nota['nota'])

for aluno in alunos_agrupados:
    print(aluno)

print()
grupos = groupby(alunos_agrupados, key=lambda nota: nota['nota'])

for chave, grupo in grupos:
    print(chave)
    
    for aluno in grupo:
        print(aluno)
