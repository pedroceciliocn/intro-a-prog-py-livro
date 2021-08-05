"""
Exercício 8.3 Escreva uma função que receba o lado de um quadrado e retorne sua
área (A = lado²).
Valores esperados:
área_quadrado(4) == 16
área_quadrado(9) == 81
"""
def área_quadrado(lado):
    """retorna a área, dado o lado do quadrado"""
    return lado**2

print(área_quadrado(4))
print(área_quadrado(9))