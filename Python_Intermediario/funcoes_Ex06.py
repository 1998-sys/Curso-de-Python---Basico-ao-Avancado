"""

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def converter_horario(horas, minutos):
    if horas == 0:
        return 12, minutos, 'A'
    elif horas < 12:
        return horas, minutos, 'A'
    elif horas == 12:
        return 12, minutos, 'P'
    else:
        return horas - 12, minutos, 'P'

def exibir_horario(horas, minutos, periodo):
    periodo_str = 'A.M.' if periodo == 'A' else 'P.M.'
    print(f'{horas}:{minutos:02d} {periodo_str}')

def main():
    while True:
        try:
            horas = int(input("Digite as horas (0-23): "))
            minutos = int(input("Digite os minutos (0-59): "))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                horas_12, minutos_12, periodo = converter_horario(horas, minutos)
                exibir_horario(horas_12, minutos_12, periodo)
            else:
                print("Horas ou minutos inválidos. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        
        repetir = input("Deseja converter outro horário? (s/n): ").strip().lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()