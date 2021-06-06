deposito_inicial = float(input("De o deposito inicial: "))
taxa = float(input("De a taxa de juros mensal em %: "))
n = 1
acumulado = deposito_inicial
while n <= 24:
    acumulado = acumulado + (acumulado * (taxa/100))
    print(f"Saldo acumulado disponível no mês {n} é de R${acumulado:.2f}.")
    n = n + 1
print(f"O total ganho com juros foi de R${acumulado - deposito_inicial:.2f}.")

