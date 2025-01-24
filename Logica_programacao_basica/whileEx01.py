"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""


n = input('Informe um valor: ')

while True:
    try:
        n = float(n)
        if 0 <= n <=10:
            print(f'{n} está correto, dentro da faixa permitida 0 a 10!')
            break
        else:
            n = input('Tente novamente o valor não está no range permitido: ')
            
    
    except:
        n = input('Valor não numérico tente novamente: ')

    