"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
"""

salario = input('informe seu salário atual: ')

if float(salario) >= 1500:
    aumento = float(salario) * 0.05
    n_salario = float(salario) + aumento
    print(f'Seu salario era R${float(salario):.2f}, o percentual aplicado foi de 5% com um valor de aumento de R${aumento:.2f}\n'
          f'Logo seu novo salário será {n_salario:.2f}')
elif 700 < float(salario) < 1500:
    aumento = float(salario) * 0.10
    n_salario = float(salario) + aumento
    print(f'Seu salario era R${float(salario):.2f}, o percentual aplicado foi de 10% com um valor de aumento de R${aumento:.2f}\n'
          f'Logo seu novo salário será {n_salario:.2f}')
elif 280 < float(salario) <= 700:
    aumento = float(salario) * 0.15
    n_salario = float(salario) + aumento
    print(f'Seu salario era R${float(salario):.2f}, o percentual aplicado foi de 15% com um valor de aumento de R${aumento:.2f}\n'
          f'Logo seu novo salário será {n_salario:.2f}')
else:
    aumento = float(salario) * 0.20
    n_salario = float(salario) + aumento
    print(f'Seu salario era R${float(salario):.2f}, o percentual aplicado foi de 20% com um valor de aumento de R${aumento:.2f}\n'
          f'Logo seu novo salário será {n_salario:.2f}')
