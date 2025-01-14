"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo

"""

hora = input('Informe o valor ganho por hora: ')
bruto = float(hora)*8*30
inss = bruto*0.05
sindicato = bruto * 0.11
liquido = bruto - (inss + sindicato)

print(f'O Salário bruto é R${bruto}, foi pago R${inss} ao INSS e R${sindicato} ao sindicato \n'
      f'Já o salário líquido é R${liquido}')