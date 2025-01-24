"""
Repetições 
while (equanto)

Executa uma ação enquanto uma condição for verdadeira

Loop Infinito -> quando um código não tem fim
"""

condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':

#         break  # para o laço while

# print('Acabou')


# Além de utilizar o Brake podemos fazer a condição ser FALSE em determinado momento.

#contador = 0

# while contador < 10:
#     print(contador)
#     contador +=1
"""
Operadores de atribuição

= ; += ; -= ; *= ; /= ; //= ; **= ; %= 
"""

# while + continue (pula o laço)

# contador = 0
# while contador <= 100:
#     contador +=1
    

#     if contador == 6:
#         print('não vou printar o 6')
#         continue
#     print(contador)

#     if contador == 40:
#         break


# While - Laços internos

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1

# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'linha[{linha}], Coluna[{qtd_colunas}]')
#         coluna +=1

#     linha +=1



nome = 'Matheus Bandeira'

tamanho = len(nome)
print(tamanho)
letra = 0

while letra < tamanho:
    print(nome[letra])
    letra +=1