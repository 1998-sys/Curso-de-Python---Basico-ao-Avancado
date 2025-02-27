# encoding do arquivo

caminho = 'C:\\Users\\Matheus\\Documents\\Udemy - Python\\Python_Intermediario\\'
caminho += 'encoding.txt'

with open(caminho, 'a+', encoding='utf-8') as arquivo:
    arquivo.write('Olá mundo\n')
    arquivo.write('Atenção\n')

# os.remove(caminho_arquivo) -> remove o arquivo
#os.rename(caminho, nome) -> renomeia o arquivo
