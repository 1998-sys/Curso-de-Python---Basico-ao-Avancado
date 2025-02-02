"""
Try, excpet, else e finally

É importante informar o erro que irá ocorrer
"""
a = 18
b = 2


try:
    c =  a / b
    print('linha1'[1000]) # gerando erro fora do índice
except ZeroDivisionError:
    print('Dividiu por Zero.')
except NameError:                  #dá para incluir várias excessões 
    print('Nom b não está definido')
except (TypeError, IndexError) as error: # é possível passar mais de um erro e também armazenar o erro para imprimir
    print('TypeError')
    print('MSG: ', error) # mensagem do erro
    print('Nome: ', error.__class__.__name__) # Nome do erro
except Exception: # Generaliza qualquer erro, isso é uma má prática
    print('Erro desconhecido')

print('CONTINUAR')