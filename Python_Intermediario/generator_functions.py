"""
Intrdoção às Generator functions em python 
Generator = Função que sabe pausar
"""

# def generator(n=0):
#     yield 1 # Pausa a execução da função
#     print('Continuando.....')
#     yield 2 
#     print('Mais uma vez...')
#     yield 3 
#     print('Vou terminar')
#     return 'Acabou'

# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)


def generator(n=0, maximum = 10):
    while True:
        yield n
        n +=1

        if n > maximum:
            return
        
gen = generator()
for n in gen:
    print(n)