# Programa 6.9 - Pesquisa sequencial
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0
achou = False
while achou == False and x < len(L):
    if L[x] == p:
        achou = True
    x += 1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")
