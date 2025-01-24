"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pop_A = 80000
tx_a = 0.03
pop_b = 200000
tx_b = 0.015

anos = 0
while True:
    if pop_A != pop_b:
        pop_A = pop_A + (pop_A * tx_a)
        pop_b = pop_b + (pop_b * tx_b)

        anos +=1
    else:
        print(f'Serão necessários {anos} anos para que a população do país A se iguale com B.')
        break
