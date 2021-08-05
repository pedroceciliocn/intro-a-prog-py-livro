def soma(L):
    total = 0
    for e in L:
        total += e
    return total

def média(L):
    return soma(L)/len(L)

L = [10, 20, 25, 30]
print(soma(L))
print(média(L))

#alternativa
def média(L):
    total = 0
    for e in L:
        total += e
    return total / len(L)

print(média(L))