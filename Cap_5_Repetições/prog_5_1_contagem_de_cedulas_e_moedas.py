# Programa 5.1 - Contagem de cédulas
valor = float(input("Digite o valor a pagar: "))
cédulas = 0
moedas = 0
atual = 100
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cédulas += 1
    else:
        if atual >= 1:
            print(f"{cédulas} cédula(s) de R${atual}.")
        else:
            print(f"e {cédulas} moeda(s) de {atual*100:.0f} centavo(s).")
        if a_pagar < 0.01:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cédulas = 0
