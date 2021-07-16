"""
Exercício 7.1 Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""
s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a string a ser pesquisada: ")
while len(s_2) > len(s_1):
    s_2 = input("Dê a string a ser pesquisada (menor que a primeira): ")


p = s_1.find(s_2)
if p == -1:
    print(f"{s_2} não foi encontrado em {s_1}")
else:
    print(f"{s_2} encontrado na posição {p} de {s_1}")



