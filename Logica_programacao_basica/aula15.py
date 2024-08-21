# Formatação de strings com o método format

a = 'AAAA'
b = 'BBBBB'
c = 1.1
# Na ordem vem o primeiro argumento da função format
string = 'a={0} a= {0}b={1} c{2:.2f}'
formato = string.format(a,b,c)

print(formato)