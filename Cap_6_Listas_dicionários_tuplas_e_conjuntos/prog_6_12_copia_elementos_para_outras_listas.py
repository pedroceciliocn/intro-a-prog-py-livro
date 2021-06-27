# Programa 6.12 - Cópia de elementos para outras listas
V = [9, 8, 7, 12, 0, 13, 21] #valores
P = [] #pares
I = [] #ímpares
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print(f"Pares: {P}")
print(f"Ímpares: {I}")