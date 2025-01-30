perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '4', '5', '6'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['10', '15', '25', '30'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['3', '4', '5', '6'],
        'Resposta': '5'
    }
]

acertos = 0
for dicionario in perguntas:
    print(f"{dicionario['Pergunta']}")

    for indice, opcao in enumerate(dicionario['Opcoes'], start=1): # for para iterar nas opções
        print(f'{indice}) {opcao}')

    resposta = input('Informe sua resposta: ')
    if resposta == dicionario['Resposta']:
        print('Acertou! 👍')
        acertos +=1
    else:
        print('Errou! 👎')

print(f'Você obteve {acertos} acertos !')
