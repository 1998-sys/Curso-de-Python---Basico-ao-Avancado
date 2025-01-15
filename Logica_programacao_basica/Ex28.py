"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

# Solicitar entrada do usuário
valor_hora = float(input("Digite o valor da sua hora trabalhada: R$ "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

# Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Determinar o desconto do IR
if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20

# Calcular os outros descontos
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

# Calcular o total de descontos e o salário líquido
total_descontos = desconto_ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

# Exibir os resultados
print("\n===== Folha de Pagamento =====")
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir / salario_bruto * 100:.0f}%) : R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")