#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

ganho_hora  = input('Informe o valor da hora trabalhada: ')
hora_trabalho = input('Informe a quantidade de horas trabalhadas no mês: ')

print(f'Seu salário total será: {float(ganho_hora) * float(hora_trabalho)}')
