from sys import path

#print(*path, sep='\n')

from package_99.modulo import soma # importa somente a função soma 
from package_99.modulo import mult

from package_99 import modulo # importa todo o módulo


total = soma(1,2)
print(total)

total2 = mult(3,2)
print(total2)
