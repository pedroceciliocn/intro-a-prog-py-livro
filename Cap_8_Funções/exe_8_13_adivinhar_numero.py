"""Exercício 8.13* Altere o Programa 8.20 de forma que o usuário tenha três chances
de acertar o número. O programa termina se o usuário acertar ou errar três vezes."""

# # Programa 8.13
# import random
# n = random.randint(1, 10)
# x = int(input("Escolha um número entre 1 e 10: "))
# if x == n:
#     print("Você acertou!")
# else:
#     print("Você errou.")

# Exercício
import random
n = random.randint(1, 10)
# continuar = True
tentativas = 0
# x = int(input("Escolha um número entre 1 e 10: "))
# while continuar == True:
#     contador += 1
#     if x != n:
#         if contador == 3:
#             continuar = False
#         else:
#             print(f"Você errou {contador} vezes.")
#             x = int(input("Escolha um número entre 1 e 10: "))
#     else:
#         continuar = False
#         print("Você acertou!")   
    
while tentativas < 3:
    x = int(input("Escolha um número entre 1 e 10: "))
    if x == n:
        print("Você acertou!")
        break
    else:
        print(f"Você errou.")
    tentativas += 1
    
    
          