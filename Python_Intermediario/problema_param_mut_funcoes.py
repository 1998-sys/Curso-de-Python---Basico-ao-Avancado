# problema dos parâmetros mutáveis em função pyhton


# None é a melhor forma de resolver o problema
def adiciona_clientes(nome, lista=None): # o python reutiliza a lista e não reinicia novamente
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

#primeira forma simples de resolver o problema
lista_1 = []
cliente1 = adiciona_clientes('Luiz', lista_1)
adiciona_clientes('Joana', cliente1)
print(cliente1)


cliente2 = adiciona_clientes('helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)