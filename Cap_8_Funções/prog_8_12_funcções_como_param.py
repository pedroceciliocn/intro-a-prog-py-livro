# Programa 8.12 - Funções como parâmetro
def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def imprime(a, b, func_oper):
    print(func_oper(a, b))

imprime(5, 4, soma)
imprime(10, 1, subtração)

