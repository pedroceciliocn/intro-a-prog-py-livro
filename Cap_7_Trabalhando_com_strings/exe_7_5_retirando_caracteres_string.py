"""
Exercício 7.5 Escreva um programa que leia duas strings e gere uma terceira, na
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA
"""
s_1 = input("Dê a primeira sting: ")
s_2 = input("Dê a segunda string: ")
s_3 = ""
while len(s_2) > len(s_1):
    s_2 = input("Dê a segunda string (que não seja maior que s_1): ")

for i in s_1:
    if i not in s_2:
        s_3 += i

if s_3 == "":
    print("A string está vazia pq todos os caracteres  de s_1 foram removidos")
else:
    print(s_3)