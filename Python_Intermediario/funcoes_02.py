"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""

def soma (x,y,z):
    print(f'{x=}  {y=}', '|', 'x + y = ', x + y)

soma(1,2,3)
soma(y=2, x=1,z=3)

# Toda vez que eu nomei um argumento os próximos deverão ser nomeados
soma(1, y=2, z=3)