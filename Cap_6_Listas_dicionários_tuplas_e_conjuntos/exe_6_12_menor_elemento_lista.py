# Exercício 6.12 - Verificação do menor valor
L = [1, 7, 2, 4]
mínimo = L[0] #inicializando o min com o valor do primeiro. Poderiamos usar o 0, desde que nao houvessem negativos na lista
for e in L:
    if e < mínimo:
        mínimo = e
print(mínimo)