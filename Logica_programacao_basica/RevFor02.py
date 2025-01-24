"""
For + Range
range -> range(start, stop, step)

range -> contagem começa em 0
"""

# numeros = range(0,100,8)

# for numero in numeros:
#     print(numero)

for i in range(10):
    if i==2:
        print('i é 2, pulando...')
        continue
    if i ==8:
        print('i é 9, seu else não executará')
        break
    for j in (1,3):
        print(i,j)
else:
    print(f'For completo com Sucesso !')