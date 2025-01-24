"""
Faça um jogo para o usuário adivinha qual a palavra secreta.
- você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; Exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *

    Faça uma contagem de tentaticas do seu usuário


"""
import os

p_secreta = 'mico'
tentativas = 0
letras_acertadas = ''

print('JOGO DA FORCA'.center(50))

while True:
    letra = input('informe uma letra: ')
    tentativas +=1
    if len(letra) > 1:
        print('digite apenas uma letra: ')
        continue
    if letra in p_secreta:
        letras_acertadas += letra
    
    palavra_formada = ''
    for letra_secreta in p_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == p_secreta:
        os.system('cls')
        print(f'Você ganhou ! Parabéns {tentativas} tentativas')
        letras_acertadas =''
        tentativas = 0
        break
    