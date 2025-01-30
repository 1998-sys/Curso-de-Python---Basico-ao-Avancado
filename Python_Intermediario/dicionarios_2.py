"""
Manipulando chaves e valores em dicionários
"""
pessoa = {
    'nome':'Matheus Bandeira',
    'sobrenome':'Miranda',
    'idade': 26,
    'altura': 1.80,
    'enderecos': [{'Rua':'x','numero':123},
                  {'Rua': 'b', 'bairro': 'y'}],
}


pessoa['nome']= 'João' # Alterando o valor de uma chave

pessoa['teste'] = 'teste' # Adicionando uma nova chave

del pessoa['teste'] # Deletando uma chave

# verificando se a chave existe
if pessoa.get('teste') is None:
    print('Chave não existe')
else:
    print(pessoa['teste'])




