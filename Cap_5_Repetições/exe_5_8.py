n_1 = int(input("Digite o primeiro numero:"))
n = n_1
n_2 = int(input("Digite o segundo numero:"))
resultado = 0
if n_1 < n_2:
    while n <= n_2:
        resultado = n + n_2 
        n = n + 1
    print(f"{n_1}x{n_2} = {resultado}")

if n_1 > n_2:
    n_1,n_2 = n_2,n_1
    while n <= n_2:
        resultado = n + n_2 
        n = n + 1
    print(f"{n_2}x{n_1} = {resultado}")
