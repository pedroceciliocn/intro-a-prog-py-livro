# Programa 6.11 - Verificação do maior valor
L = [1, 7, 2, 4]
máximo = L[0] #inicializando o max com o valor do primeiro. Poderiamos usar o 0, desde que nao houvessem negativos na lista
for e in L:
    if e > máximo:
        máximo = e
print(máximo)