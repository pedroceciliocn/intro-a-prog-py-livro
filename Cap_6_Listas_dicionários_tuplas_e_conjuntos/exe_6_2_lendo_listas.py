#6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
L_1 = []
L_2 = []

while n != 0:
    n = int(input("Dê um numero para a lista 1 (0 para sair)"))
    L_1.append(n)
while n != 0:
    n = int(input("Dê um numero para a lista 2 (0 para sair)"))   
    L_2.append(n)

L_3 = L_1[:]
L_3.extend(L_2)
x = 0
while x < len(L_3):
    print(x, L_3[x])
    x += 1
print(L_3)
