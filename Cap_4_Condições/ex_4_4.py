salario = float(input("De o seu salario: "))
aumento = 0
if salario > 1250:
    aumento = 0.10 * salario
if salario <= 1250:
    aumento = 0.15 * salario
print(f"O seu aumento será de R${aumento:.2f}.")
