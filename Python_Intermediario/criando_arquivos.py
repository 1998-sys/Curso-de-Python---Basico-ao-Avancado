"""
Criando arquivos com python
usamos a função open para abrir
Um arquivo em python (ele pode ou não existir)

Modos:
- r (leitura), w(escrita), x(para criação)
- a (escreve ao final), b(binário)
- t(modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)

Mátodos úteis
write, read (escrever e ler)
writelines (esvrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

vamos falar mais sobre o módulo json, mas:
json.dump = gera um arquivo json
json.load


"""



caminho_arquivo = 'C:\\Users\\Matheus\\Documents\\Udemy - Python\\Python_Intermediario\\'
caminho_arquivo += 'criando_arquivos.txt'


# w+ - escreve e lê
with open(caminho_arquivo, 'w+') as arquivo: # já abre e fecha o arquivo automaticamente
    arquivo.write('linha 1\n') # quebra a linha
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4 \n')
    )
    arquivo.seek(0,0) # retorna o cursor para o início
    print(arquivo.read())
    print('Arquivo vai ser fechado')
    arquivo.seek(0,0)
    print(arquivo.readline().strip())  # Lendo apenas uma linha
    print(arquivo.readline().strip())  # Lendo apenas uma linha
    print('READLINES')

print('#' *40)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())


# w apaga tudo que tem no arquivo e escreve novamente 
# a não apaga nada e começa do final 