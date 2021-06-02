velocidade = float(input("De a velocidade do carro quando passou no radar: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado em R${multa:.2f}!")
if velocidade <= 80:
    print("Você não foi multado.")
