L = [1, 2, 3, 4, 5]
fim = 5 
while fim > 1: 
    trocou = False
    x = 0
    while x < (fim - 1): 
        if L[x] > L[x + 1]: # nunca entra no if
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1 # x = 1
    if not trocou: # depois da o break e sai pro for
        break
    fim -= 1
for e in L:
    print(e)