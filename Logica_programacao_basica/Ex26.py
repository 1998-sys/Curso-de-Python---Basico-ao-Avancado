"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turnos = ['M', 'V', 'N']

opcao = input('Informe seu turno:\nM-matutino\nv-vespertino\nN-noturno')

if opcao.upper() == 'M':
    print('Bom dia !')
elif opcao.upper() ==  'V':
    print('Boa Tarde!')
elif opcao.upper() == 'N':
    print('Boa Noite')
else:
    print('Valor inválido')