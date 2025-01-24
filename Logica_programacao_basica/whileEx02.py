"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""

nome = input('Informe seu nome: ')
senha = input('Informe sua senha: ')

while True:
    if nome == senha:
        print('Erro nome e senha não podem ser o mesmo !')
        senha = input('Informe outra senha: ')
    else:
        print('Usuário cadastrado')
        break