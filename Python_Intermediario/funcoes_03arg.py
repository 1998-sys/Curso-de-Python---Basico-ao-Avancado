"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será usado.

Refatorar.

"""
# Toda a vez que tenho um parâmetro com valor padrão todos os outros a sua frente devem receber um valor padrão
def soma(x,y, z=None): # quando temos um parâmetro que pode ou não ser enviado, deverá ser None (utilizar comparação)
    if z is not None:
        print( f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1,2)
soma(3,5)
soma(100 , 200)
soma(100, 200 , 0)
soma(x=7, z=0, y=7)
