from texttable import Texttable


texto = input('informe o ano: ')

tabela = Texttable()
alg = int(texto[2:])

if alg != 0:
    resultado = alg % 4
    if resultado == 0:
        tabela.add_rows([['ANO', 'RESULTADO'], [texto, 'É BISSEXTO !']])
        print(tabela.draw())
    else:
        tabela.add_rows([['ANO', 'RESULTADO'], [texto, 'NÃO É BISSEXTO !']])
        print(tabela.draw())
    
else:
    ano = int(texto)
    resultado = ano % 400
    
    if resultado == 0:
        tabela.add_rows([['ANO', 'RESULTADO'], [texto, 'É BISSEXTO !']])
        print(tabela.draw())
    else:
        tabela.add_rows([['ANO', 'RESULTADO'], [texto, 'NÃO É BISSEXTO !']])
        print(tabela.draw())
