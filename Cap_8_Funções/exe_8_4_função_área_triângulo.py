"""
Exercício 8.4 Escreva uma função que receba a base e a altura de um triângulo e
retorne sua área (A = (base x altura) / 2)
Valores esperados:
área_triângulo(6, 9) == 27
área_triângulo(5, 8) == 20
"""
def área_triângulo(base, altura):
    """retorna a área de um triângulo, dadas base e altura"""
    return ((base*altura)/2)

print(área_triângulo(6, 9))
print(área_triângulo(5, 8))