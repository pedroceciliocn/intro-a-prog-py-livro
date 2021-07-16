"""
Exercício 7.4 Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""
s = input("Dê uma string: ")
contador = {}

for letra in s:
    contador[letra] = contador.get(letra, 0) + 1

for key, value in contador.items():
    print(f"{key}: {value}x")

