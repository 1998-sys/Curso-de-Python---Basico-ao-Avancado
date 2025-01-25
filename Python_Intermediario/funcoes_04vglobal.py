"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançável
O escopo local é  escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 10 # Variável global
 
def escopo():
    x = 1  # variável local
    global y # definindo uma variável como global
    y = 22
    print(x)

escopo()

print(x)  # não definido pois só podemos acessar as variáveis da função fora da função
print(y) # puxando a variável global dentro da função