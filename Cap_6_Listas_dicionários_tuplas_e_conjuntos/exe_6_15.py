L = [3, 3, 1, 5, 4]
fim = 5 
while fim > 1: 
    trocou = False
    x = 0
    while x < (fim - 1): 
        if L[x] > L[x + 1]: # nao entra no if de primeira
            trocou = True
            temp = L[x] 
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1  # passa pro proximo e começa a comparar o segundo 3 com o 1 e continua
    if not trocou: 
        break
    fim -= 1
for e in L:
    print(e)