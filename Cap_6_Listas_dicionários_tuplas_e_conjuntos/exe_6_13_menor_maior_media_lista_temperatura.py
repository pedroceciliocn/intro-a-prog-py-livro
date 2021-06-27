# Exercício 6.13 - Verificação da menor, maior e media de temperatura usando lista
T = [-10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0] 
máxima = T[0]
soma = 0
n = 0
for e in T:
    if e < mínima:
        mínimo = e
    if e > máxima:
        máxima = e
    soma += e
    n += 1
print(f"A mínima foi de {mínima}, a máxima de {máxima} e a média de {soma/n:.0f}.")