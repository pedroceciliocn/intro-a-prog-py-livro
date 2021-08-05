"""
Exercício 8.1 Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5, 6) == 6
máximo(2, 1) == 2
máximo(7, 7) == 7
"""
def máximo(a, b):
    """retorna o maior de dois números"""
    if a >= b:
        return a
    else:
        return b

print(máximo(5, 6))
print(máximo(2, 1))
print(máximo(7, 7))