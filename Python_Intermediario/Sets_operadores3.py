"""
Operadores úteis:

união -> | -> une o set
interseção -> & -> Retorna os valores que estão presentes em ambos os sets
diferença -> - -> Retorna os valores que estão presentes no primeiro set e não no segundo
diferença simétrica -> ^ -> Retorna os valores que estão presentes em um set e não no outro

"""
s1 = set((1,2,3))
s2 = set((2,3,4))
s3 = s1 | s2
print(f'A união de s1 e s2 é {s3}')
s4 = s1 - s2
print(f'A diferença de s1 e s2 é: {s4}')
s5 = s1 ^ s2
print(f'A diferença simétrica é {s5}')