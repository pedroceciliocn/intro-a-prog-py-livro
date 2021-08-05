# Programa 8.10 - Função com parâmetros obrigatórios e opcionais
def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s

soma(2, 3)
soma(2, 3, True)