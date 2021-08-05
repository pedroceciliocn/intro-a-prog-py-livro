"""
Exercício 8.6 Reescreva o Programa 8.2 de forma a utilizar for em vez de while.
"""
# Programa 8.2 - corrigido (genérico) e com for
def soma(L):
    total = 0
    for x in range(len(L)):
        total += L[x]
    return total

L = [1, 7, 2, 9, 15]
print(soma(L)) # deu certo
print(soma([7, 9, 12, 3, 100, 20, 4])) # agora também deu certo, pois ela é genérica o suficiente