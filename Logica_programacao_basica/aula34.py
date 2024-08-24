"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Ter cuidado para não cair em looping infinito -> quando um código não tem fim 
"""

condicao = True
while condicao:
    nome = input('Qual o seu nome ? ')
    print(f'Seu nome é {nome}')

    if nome == 'Sair':
        break