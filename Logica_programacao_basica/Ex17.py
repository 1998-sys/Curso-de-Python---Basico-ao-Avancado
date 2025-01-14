"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
 calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

"""

arquivo = input("informe o tamanho do arquivo em MB: ")
velocidade = input("Informe a velocidade de internet em Mbps")

print(f'O tempo estimado de dowload é {((float(arquivo)*1024*1024*8) / (float(velocidade) * 1000000)) * 60 }')