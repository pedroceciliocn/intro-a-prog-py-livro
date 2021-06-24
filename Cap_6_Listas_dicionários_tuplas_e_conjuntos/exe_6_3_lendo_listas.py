# 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
L_1 = []
L_2 = []
L = []
while l != 0:
    l = int(input("Adicione elementos para a primeira lista (0 para sair): "))
    L_1.append(l)
while l != 0:
    l = int(input("Adicione elementos para a segunda lista (0 para sair): "))
    L_2.append(l)
L_3 = L_1[:]
L_3.extend(L_2)
x = 0
while x < len(L_3):
    y = 0
    while y < len(L):
        if L_3[x] == L[y]:
            break
        y += 1
    if y == len(L):
        L.append(L_3[x])
    x += 1
x = 0
while x < len(L):
    print(f"{x}: {L[x]}")
    x += 1
print(L)