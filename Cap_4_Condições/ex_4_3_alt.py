n_1 = int(input("De o primeiro numero: "))
n_2 = int(input("De o segundo numero: "))
n_3 = int(input("De o terceiro numero: "))

maior = n_1
menor = n_1
if n_2 > n_1 and n_2 > n_3:
    maior = n_2
if n_3 > n_1 and n_3 > n_2:
    maior = n_3
if n_2 < n_3 and n_2 < n_1:
    menor = n_2
if n_3 < n_2 and n_3 < n_1:
    menor = n_3
print(f"O maior numero é {maior} e o menor é {menor}.")


#############Questão do slide da aula###########################################
n_1 = int(input("De o primeiro numero: "))
n_2 = int(input("De o segundo numero: "))
n_3 = int(input("De o terceiro numero: "))

menor = n_1

if n_2 <= n_3 and n_2 <= n_1:
    menor = n_2
if n_3 <= n_2 and n_3 <= n_1:
    menor = n_3
print(f"O menor numero é {menor}.")
