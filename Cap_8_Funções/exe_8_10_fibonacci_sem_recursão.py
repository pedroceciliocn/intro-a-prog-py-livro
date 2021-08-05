"""
Exercício 8.10 - Reescreva a função para cálculo da sequência Fibonacci, sem
utilizar recursão.
"""
def fibonacci(n):
    primeiro = 0
    segundo = 1
    while n > 0:
        primeiro, segundo = segundo, segundo + primeiro
        n -= 1
    return primeiro

for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")