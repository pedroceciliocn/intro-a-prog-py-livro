#6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
L_1 = []
L_2 = []

while True:
    l = int(input("Escolha qual lista ira adicionar elementos (1 ou 2 e 0 para sair)"))
    if l == 0:
        break
    elif l == 1:
        n = input("De um elemento e o adicionaremos a primeira lista:")
        L_1.append(n)
    elif l == 2:
        n = input("De um elemento e o adicionaremos a segunda lista:")
        L_2.append(n)

L = L_1 + L_2
x = 0
while x < len(L):
    print(L[x])
    x += 1
