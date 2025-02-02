"""
dir, hasattr, getattr em python
"""
string = "Matheus"
metodo = 'upper'
#print(string.__dir__())  # dir mostra todos os métodos disponíves para a classe

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)()) # pega e executa o método armazenado em uma váriável como string
else:
    print('Não existe o método', metodo) 