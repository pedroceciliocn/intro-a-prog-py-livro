"""
Exercício 7.3 Escreva um programa que leia duas strings e gere uma terceira apenas
com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
"""
s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string: ")
s_3 = ""

for i in s_1:
    if i not in s_2 and i not in s_3:
        s_3 += i

for i in s_2:
    if i not in s_1 and i not in s_3:
        s_3 += i

if s_3 == "":
    print("Nenhum caractere exclusivo/incomum encontrado")
else:
    print(f"Caracteres incomuns encontrados: {s_3}")