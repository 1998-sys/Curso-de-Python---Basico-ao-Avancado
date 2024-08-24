"""
Repetições
while(enquanto)

"""

contador = 0

while contador <=100:
    contador +=1
    if contador == 6:  # pula o 6° laço - não executa o que está abaixo
        continue

    print(contador)

    if contador == 40:
        break
    