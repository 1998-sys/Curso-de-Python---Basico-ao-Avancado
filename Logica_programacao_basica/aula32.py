"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que nãi é um número inteiro 
"""

numero = input('Digite um número inteiro: ')

try:
     numero_int = int(numero) # int só convert uma string de formato int, se tentar um float não funciona
     if numero_int % 2 == 0:
         print(f'{numero_int} é par !')
     else:
         print(f'{numero_int} é ímpar !')
except:
     print(f'Você digitou {numero}, e não é inteiro ou número.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada Ex.
Bom dia 0-11, boa tarde 12 - 17 e boa noite 18-23

"""
hora = input('informe a hora: ')

try:
    hora_int = int(hora)
    if 0 <= hora_int <= 11:
        print(f'{hora_int}, Bom dia')
    elif 12 <= hora_int <= 17:
        print(f'{hora_int}, Boa Tarde')
    else:
        print(f'{hora_int}, Boa noite')
except:
    print('Formato Inválido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto", se tiver entre 5 e 6 letras, escreva
"Seu nome é normal", "maior que 6 escreva "Seu nome é muito grande"

"""

nome = input('Informe sue nome: ')

tamanho_nome= len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif 5 <= tamanho_nome < 6:
    print('Seu nome é normal')
elif tamanho_nome >= 6:
    print('Seu nome é muito grande')