# Formatação de strings com o método format

a = 'AAAA'
b = 'BBBBB'
c = 1.1
# Na ordem vem o primeiro argumento da função format
# string = f'a={0} a= {0}b={1} c{2:.2f}'  #2.f formata as casa decimais
# formato = string.format(a,b,c)



# Formatação utilzando o comando format
formato = 'a={0} b={1} c={2:.3f}'.format(a,b,c) # As chaves refereciam os valores também é possível utilizar índices
print(formato)