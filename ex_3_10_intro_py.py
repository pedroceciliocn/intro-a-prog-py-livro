salario = float(input("De o seu salario: "))
aumento = float(input("De o seu aumento em %: "))

aumento = aumento/100
salario_final = salario + salario*aumento
print(f"Seu salario com aumento é de R${salario_final:.2f}.")
