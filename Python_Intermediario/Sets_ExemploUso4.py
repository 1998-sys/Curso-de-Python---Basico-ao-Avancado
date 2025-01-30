"""
Exemplo de uso
"""

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
