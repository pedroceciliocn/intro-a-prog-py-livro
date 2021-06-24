#6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
L_1 = []
L_2 = []

while True:
    n = int(input("Dê um numero da lista 1 (0 para sair)"))
    if n == 0:
        break
    L_1.append(n)
while True:
    n = int(input("Dê um numero da lista 2 (0 para sair)"))   
    if n == 0:
        break
    L_2.append(n)

L_3 = L_1[:]
L_3.extend(L_2)
x = 0
while x < len(L_3):
    print(x, L_3[x])
    x += 1
print(L_3)
