"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.

- Se a letra digitado estinar na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *

Faça uma contagem de tentivas do usuário
"""
import os 

palavra = 'Abacate'.upper()
tentativas = 1
letras_acertada = ''

print('Tente Advinhar a palavra')
while True:
    letra = input(f'{tentativas}º tentativa informe a letra: ').upper()

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra:
        print(f'Acertou a letra "{letra}" está contida na palavra ')
        letras_acertada += letra

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    tentativas +=1

    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('Você Ganhou ! Parabéns')
        print('A palavra era', palavra_formada)
        print('Tentativas: ', tentativas)
        break