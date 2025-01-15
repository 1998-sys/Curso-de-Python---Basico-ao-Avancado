"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

notas = []
n1 = input('informe a primera nota: ')
n2 = input('infomre a segunda nota: ')

notas.append(float(n1))
notas.append(float(n2))

media = sum(notas)/len(notas)
if media >= 10:
    print(f'Nota final {media}, aprovado com distinção !')
elif media >= 7:
    print(f'Nota {media}, aprovado !')
else:
    print(f'Nota {media}, reprovado !')