# exercicio 6.9 - Pesquisa sequencial sem variavel achou com dois valores
L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = 0
y = 0
while x < len(L) and L[x] != p:
    x += 1
if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")

while y < len(L) and L[y] != v:
    y += 1
if y < len(L):
    print(f"{v} achado na posição {y}")
else:
    print(f"{v} não encontrado")

