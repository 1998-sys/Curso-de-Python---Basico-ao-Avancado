"""
Imutáveis: str, int, float, bool
"""
string = 'Luiz Otávio'
print(string[3])
# string[3] = 'j' # imutável não dá para fazer a alteração
# Outra forma 
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string.zfill(100))
