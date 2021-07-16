"""
Exercício 7.6 Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA
"""
s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string (a ser substituída na primeira): ")
s_3 = input("Dê a terceira string (a substituir a segunda na primeira): ")
s_4 = ""

while len(s_2) != len(s_3):
    print("As duas devem ter o mesmo tamanho!")
    s_2 = input("Dê a segunda string (a ser substituída na primeira): ")
    s_3 = input("Dê a terceira string (a substituir a segunda na primeira): ")

for i in s_1:
    p = s_2.find(i)
    if p != -1:
        s_4 += s_3[p]
    else:
        s_4 += i
    
print(f"{s_2}\'s foram substituídos por {s_3}\'s em {s_1}, gerando: ")
print(f"{s_4}")


