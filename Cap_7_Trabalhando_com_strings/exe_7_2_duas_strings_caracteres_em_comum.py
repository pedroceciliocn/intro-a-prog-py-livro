"""
Exercício 7.2 Escreva um programa que leia duas strings e gere uma terceira com
os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
3ª string: CBT
"""
s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string: ")
s_3 = ""
while len(s_1) < len(s_2):
    s_2 = input("Dê a segunda string (menor que a primeira):")

for i in s_1:
    if i in s_2 and i not in s_3:
        s_3 += i

if s_3 == "":
    print(f"Não foi encontrado nada em comum entre {s_1} e {s_2}")
else:
    print(f"Caracteres em comum encontrados: {s_3}")

