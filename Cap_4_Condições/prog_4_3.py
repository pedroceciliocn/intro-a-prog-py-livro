# Programa 4.3 - Cálculo do Imposto de Renda
salário = float(input("Digite o salário para cálculo do IR: "))
base = salário
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20) #nesse caso só oq passa dos primeiros 1000 é taxado
print(f"Salário: R${salário:6.2f} \nImposto a pagar: R${imposto:6.2f}")

#os 1k primeiros não são taxados, o que falta para 3k é em 20% e o que passa dos 3k em 35%
