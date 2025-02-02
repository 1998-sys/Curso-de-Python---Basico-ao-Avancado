"""
try, except, else e finally

finally -> sempre será executado !!!!
"""
try:
    8/0
    print(1)
    # exemplo abrir arquivo
except ZeroDivisionError:
    print('DIVIDIU ZERO')

else: # é executado caso não ocorra erro
    print('Não deu erro')

finally: # Finally sempre será executado
    print('Fechar Aquivo')