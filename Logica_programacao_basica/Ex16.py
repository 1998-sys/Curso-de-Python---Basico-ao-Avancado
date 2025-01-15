"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""
area = input('Informe em metros quadrados o tamanho da área a ser pintada: ')

litros = float(area)/3
qtd_latas = litros // 18

print(f'Para pintar uma área de {area} metros quadrados serão necessárias {qtd_latas} latas\n' 
      f'O preço todal é R${qtd_latas*80.:2f}')

