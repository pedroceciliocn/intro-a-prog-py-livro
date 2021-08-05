"""
Exercício 8.8 - Usando a função mdc definida no exercício anterior, defina uma função
para calcular o menor múltiplo comum (M.M.C.) entre dois números."""

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

print(mmc(9, 2))
print(mmc(-9, -2))