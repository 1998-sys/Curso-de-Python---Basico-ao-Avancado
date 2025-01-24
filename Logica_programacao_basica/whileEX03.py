"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

sexo_l = ['f','m']
e_civil = ['s','c','v','d']

nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
salario = input('Informe seu salário: ')
sexo = input('Informe o Sexo [M]asculino [F]emino: ')[0].lower()
estado = input('Informe seu estado cívil - [S]olteiro, [C]asado, [v]iúvo, [D]ivorciado: ')[0].lower()

#c_idade = idade < 0 and idade > 150
#_sal = salario < 0

while True:
    try:
        idade = int(idade)
        salario = float(salario)
        if len(nome) <= 3:
            nome = input('Informe um nome maior que 3 caracteres: ')
        elif idade < 0 and idade > 150:
            idade = input('Informe a idade correta (0 a 150 anos): ')
        elif salario <= 0:
            salario = input('Informe seu salário correto:  ')
        elif sexo not in sexo_l:
            sexo = input('Informe o sexo corretamente: ')
        elif estado not in e_civil:
            estado = input('Informe o estado cívil correto: ')
        else:
            print(f'{nome=}\n{idade=}\n{salario=}\n{sexo=}\n{estado=}')
            break
    except:
        print('Idade ou Salário não foram declarados corretamente !')
        idade = input('Informe sua idade correta: ')
        salario = input('Informe seu salário correto: ')