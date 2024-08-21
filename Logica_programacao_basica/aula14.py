# IMC - Exercício

nome = 'Matheus Bandeira'
altura = 1.83
peso = 95
imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura\npesa', peso, 'quilos e seu IMC é ', imc
      )

# place holder - elipses (vai escrever um código mais ainda não desenvolveu)

teste  = ...
print(teste) # Elipses

################# F - String ###############

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}')  #:.2f (trata as casas decimais)

# Fazer as divisõe do numero inteiro com vírgula
total = 10000.40
print(f'{total:,.2f}')


