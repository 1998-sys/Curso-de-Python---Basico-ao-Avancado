"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro
"""

i = 1
string = ''
while i<=20:
    print(i)
    string += f'{str(i)}\t'
    i+=1

print(string)