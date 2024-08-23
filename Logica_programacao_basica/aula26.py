"""
Formatação básica de Stings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0 > -100 , .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # espaço a direita
print(f'{variavel: <10}') # Espaço a esquerda
print(f'{variavel: ^10}') # Centro
print(f'{1000.1235468798:.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')