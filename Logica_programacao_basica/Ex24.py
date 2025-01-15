# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

precos = []
qtd = input(f'Informe a quantidade de produtos a cadastrar o preço: ')

for item in range(0, int(qtd)):
    valor = input(f'informe o valor do {int(item) + 1}° produto: ')
    precos.append(float(valor))

print(f'O produto que você deve comprar custa R${min(precos):.2f}')
print(f'*********Lista de Preços********\n{precos}')