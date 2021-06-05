fim = int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
    if x % 2 == 0: #imprime somente os pares entre 0 e 10
        print(x)
    x = x + 1
