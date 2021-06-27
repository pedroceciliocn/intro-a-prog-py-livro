# Exercício 6.11 - Adição de elementos à lista do prog 6.6, mas usando for
# L = []
# n = int(input("Digite um número (0 sai): "))
# L.append(n)
# while n!= 0:
#     n = int(input("Digite um número (0 sai): "))
#     L.append(n)

# for x in L:
#     print(x)

L = []
while True:
     n = int(input("Digite um número (0 sai):"))
     if n == 0:
         break
     L.append(n)
for e in L:
    print(e)
# O primeiro while não pôde ser convertido em for porque
# o número de repetições é desconhecido no início.