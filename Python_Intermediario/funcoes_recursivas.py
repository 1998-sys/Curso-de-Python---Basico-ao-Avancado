"""
# Funções recursivas e recursividade
São funções que podem se chamar de volta
- úteis para dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- um problema que possa ser dividido em partes menores
- um caso recursivo que resolve o pequeno problema.
- Um caso base que para a recursão

- fortial - n! = 5 * 4 * 3 * 2 * 1 = 120
"""
def recursiva(inicio=0, fim= 10):
    # caso base
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    inicio +=1
    return recursiva(inicio, fim)

recursiva()

