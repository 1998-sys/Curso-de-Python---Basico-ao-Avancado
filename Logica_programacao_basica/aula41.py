frase = 'O Python é uma linguagem de progrmação'\
'multiparadigma. '\
'Python foi criado por Guido Van Rossum.'.replace(" ", "") #Replace para remover os espaços 

print(frase)

i = 0
maior_aparicao = 0
letra = ''

while i < len(frase):
    letra_atual = frase[i]
    contagem_atual = frase.count(letra_atual)

    if maior_aparicao < contagem:
        maior_aparicao = contagem
        letra = letra_atual
    i+=1

print('A letra que apareceu mais vezes foi '
      f'"{letra}" que apareceu '
       f'{maior_aparicao}x' )