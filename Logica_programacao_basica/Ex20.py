# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválidos

letra = input('Informe uma letra: ')

if letra.upper() == 'F':
    print(f'{letra} representa o sexo Feminino')
elif letra.upper() == 'M':
    print(f'{letra} representa o sexo Masculino')
else:
    print(f'{letra} não representa um sexo')
