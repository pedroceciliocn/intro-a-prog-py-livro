n_1 = int(input("De o primeiro numero: "))
n_2 = int(input("De o segundo numero: "))
n_3 = int(input("De o terceiro numero: "))

maior = 0
menor = 0
if n_1 > n_2 and n_1 > n_3:
    maior = n_1
    if n_2 < n_3:
        menor = n_2
    elif n_3 < n_2:
        menor = n_3
if n_2 > n_1 and n_2 > n_3:
    maior = n_2
    if n_3 < n_1:
        menor = n_3
    elif n_1 < n_3:
        menor = n_1
if n_3 > n_1 and n_3 > n_2:
    maior = n_3
    if n_2 < n_1:
        menor = n_2
    elif n_1 < n_2:
        menor = n_1
print(f"{maior} é o maior número e {menor} é o menor.")
