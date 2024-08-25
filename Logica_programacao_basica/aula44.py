"""
Iterável -> str, range,  etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue se iterador

"""

# texto = iter('Matheus') # __iter__()


# # método next tá os próximos valores
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))


texto = 'Matheus'

iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
