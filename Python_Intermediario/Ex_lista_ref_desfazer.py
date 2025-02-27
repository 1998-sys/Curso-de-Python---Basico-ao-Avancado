"""
Criar uma função que armazene evalores em uma lista com 3 operações - listar tarefas (inserir e mostrar), desfazer(tira a última inclusão),
refazer (refaz a última inclusão)
"""
tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa a listar')
        return
    print('Tarefas')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa a desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()
    


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa a refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas_refazer.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefas:
        print('Você não digitou nenhuma tarefa')
        return
    tarefa = tarefas_refazer.pop()
    tarefas_refazer.append(tarefa)
    print()



while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas,tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
    