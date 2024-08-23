 # Operador lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
else:
    print('Senha incorreta')

print(not True)
print(not False)
print(not 0)