
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def valida_conversao (mensagem, tipo):
    """
    Função par solicitar a entrada do usuário e validar o tipo de dado
    -> mensagem: mensagem a ser exibida ao usuário
    -> tipo: tipo esperado na conversão

    """
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print(f'Entrada inválida ! Por favor, informe um valor do tipo {tipo.__name__}')




pop_A = valida_conversao('Informe o tamanhoa da população A: ', int)
tx_a = valida_conversao('Infomre a taxa de crescimento da população A: ', float)
pop_b = valida_conversao('Informe o tamanho da população de B: ', int)
tx_b = valida_conversao('Informe a taxa de crescimento da população de B: ', float)

anos = 0


while True:

        if pop_A != pop_b:
            pop_A = pop_A + (pop_A * tx_a)
            pop_b = pop_b + (pop_b * tx_b)

            anos +=1
        else:
            print(f'Serão necessários {anos} anos para que a população do país A se iguale com B.')
            break
   

