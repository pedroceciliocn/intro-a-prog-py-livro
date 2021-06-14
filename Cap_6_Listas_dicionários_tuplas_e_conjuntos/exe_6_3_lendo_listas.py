# 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
L_1 = []
L_2 = []
L = []
while True:
    l = int(input("Adicione elementos para a primeira lista (0 para sair): "))
    if l == 0:
        break
    else:
        L_1.append(l)
while True:
    l = int(input("Adicione elementos para a segunda lista (0 para sair): "))
    if l == 0:
        break
    else:
        L_2.append(l)

x = 0
L_3 = L_1 + L_2
while x < len(L_3):
    y = 0
    while y < len(L):
        if L_3[x] == L[y]:
            break
        y += 1
    if y == len(L):
        L.append(L_3[x])
    x += 1
z = 0
while z < len(L):
    print(f"{z}: {L[z]}")
    z += 1
