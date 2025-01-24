frase = 'O python é uma linguagem de programação'\
'multiparadigma. '\
'Python foi criado por Guido Van Rossum.'.replace(" ","")


i = 0
m_freq = 0
l_mfreq = ''
while i < len(frase):
    letra_atual = frase[i]
    cont_freq = frase.count(letra_atual)
    if m_freq < cont_freq:
        m_freq = cont_freq
        l_mfreq = letra_atual

    i +=1

print(f'A letra que apareceu mais vezes foi: {l_mfreq.upper()} e apareceu {m_freq} vezes')  
