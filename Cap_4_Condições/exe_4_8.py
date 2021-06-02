n_1 = float(input("De o primeiro numero: "))
n_2 = float(input("De o segundo numero: "))
operação = (input("Digite a operação desejada:"))

if operação == "+":
    resultado = n_1 + n_2
elif operação == "-":
    resultado = n_1 - n_2
elif operação == "*":
    resultado = n_1 * n_2
elif operação == "/":
    resultado = n_1/n_2
else:
    print("Operação inválida, digite '+', '-', '*' ou '/'ex_4_3.py")
    resultado = 0
print(f"O resultado da operação de {operação} entre {n_1} e {n_2} é: {resultado:.2f}")
