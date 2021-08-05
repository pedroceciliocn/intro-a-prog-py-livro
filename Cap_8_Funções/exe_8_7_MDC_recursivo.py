"""
Exercício 8.7 - Defina uma função recursiva que calcule o maior divisor comum
(M.D.C.) entre dois números a e b, em que a > b."""

# def mdc(a, b):
#     if b == 0:
#         return a
#     else:
#         if a > b:
#             return mdc(b, a % b)

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

