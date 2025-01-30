"""
Colocando em prática kwargs
- Cadastro de pessoa física (Vários cadastros até selecionar o opção [S]air)
- variáveis de cadastro:
    - Nome
    - Rg
    - CPF - criar função que valide
    - data de nascimento - Verificar se a data é válida
    - idade - calcula automaticamente
    - CEP
    - Cidade
    - Estado

- Utilizar **kwargs

"""
from datetime import datetime
from time import sleep

def verifica_cpf(cpf_enviado):
  while cpf_enviado.isdigit():  
        nove_digitos = cpf_enviado[:9]
        contador_regressivo = 10

        resultado_dig1 = 0
        for digito in nove_digitos:
            resultado_dig1 += int(digito) * contador_regressivo
            contador_regressivo -=1
        
        digito_1 = (resultado_dig1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        cpf_dezdigitos = nove_digitos+str(digito_1)

        contador_regressivo2 = 11
        resultado_dig2 = 0
        for digito in cpf_dezdigitos:
            resultado_dig2 += int(digito_1) * contador_regressivo2
            contador_regressivo2 -=1
        
        digito_2 = (resultado_dig2*10)%11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf_calculado == cpf_enviado:
            print('CPF Válido')
            return cpf_enviado
        else:
            print('CPF Inválido')
            cpf_enviado = input('Insira um CPF válido: ')

        

def calcula_idade(data):
    data = datetime.strptime(data, '%d/%m/%Y').date()
    data_atual = datetime.today().date()
    print(type(data_atual.year))
    idade = data_atual.year - data.year - ((data_atual.month, data_atual.day) <(data.month, data.day) ) # True or false pode ser 1 ou 0 
    return idade

def verifica_data(mensagem):
    while True:
        try:
            data = input(mensagem)
            datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            print("Data inválida. Por favor, insira no formato dd/mm/aaaa.")



def amarzena(**kwargs):
    cadastro = kwargs
    return cadastro


def main():

    operacao = ''
    print('CADASTRO PESSOA FÍSICA'.center(50))

    while True:
        operacao = input('Para sair presione a tecla [S], continuar informe qualquer outra tecla: ')[0].upper()
        if operacao != "S":    
            nome = input('informe o nome: ')
            rg = input('Informe o RG: ')
            cpf = input('Informe o cpf')
            print('Validando CPF...')
            sleep(2)
            cpf = verifica_cpf(cpf)
            data = verifica_data('Informe o ano de nascimento "dd/mm/aa": ')
            idade = calcula_idade(data)
            cep = input('Informe o CEP: ')
            cidade = input('Informe a cidade: ')
            estado = input('Informe a sigla do estado')

            cadastros = amarzena(nome=nome,rg=rg,cpf=cpf,data_nascimento = data, idade=idade, cep = cep, cidade=cidade, estado = estado)
        else:
            print('saindo do programa...')
            sleep(1)
            break
    print(cadastros)
if __name__ == "__main__":
    main()

