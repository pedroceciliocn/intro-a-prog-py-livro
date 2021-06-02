valor = int(input("Digite o valor do seu salario: "))

if valor >= 1200:
    imposto = True
else:
    imposto = False
print(f"It's {imposto} that you need to pay taxes.")
