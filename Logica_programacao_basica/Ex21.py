#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['A','E','I','O','U']

letra = input('Informe uma letra: ')

if letra.upper() in vogal:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')
