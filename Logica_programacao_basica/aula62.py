"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# print('Valor' if False else 'Outro Valor')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

digito = 9
#novo_digito = digito if digito <=9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)