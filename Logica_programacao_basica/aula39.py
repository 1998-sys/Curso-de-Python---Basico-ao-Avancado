"""
Calculadora com while
"""
while True:
    numero_1 = input('Informe o primeiro número: ')
    numero_2 = input('Informe o segundo número: ')
    operador = input('Infome o operador (+-/*)')

    numeros_validos = None #Variável que irá auxiliar na validação

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    # Verifica a validade dos números digitados
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue  

    operadores_permitidos = '+-/*'

    # Verifica se operador digitado está correto
    if operador not in operadores_permitidos:
        print('Operador Inválido')
        continue

    # Verifica se foi digitado apenas 1 operador 
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        soma  = numero_1 + numero_2
        print(f'{soma=}')
    elif operador == '-':
        subtracao = numero_1 - numero_2
        print(f'{subtracao=}')
    elif operador == '/':
        divisao = numero_1 / numero_2
        print(f'{divisao=}')
    elif operador == '*':
        multiplicaocao = numero_1 * numero_2
        print(f'{multiplicaocao=}')
    else:
        print('Não deveria acontecer')



    sair = input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
        break

