# Programa 8.7 - Função recursiva de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0)) # fibonacci com n = 0
print(fibonacci(1)) # fibonacci com n = 1
print(fibonacci(4)) # fibonacci com n = 4

