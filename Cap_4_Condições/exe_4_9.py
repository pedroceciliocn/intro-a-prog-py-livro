valor = float(input("De o valor da casa: "))
salario = float(input("De o seu salario: "))
periodo = int(input("De a quantidade de anos para quitar: "))

prestação = valor/periodo
if prestação > 0.30 * salario:
    print("Emprestimo rejeitado!")
elif prestação <= 0.30 * salario:
    print("Emprestimo aceito. As parcelas serão de R${prestação:.2f}, durante um período de {periodo} anos")
else:
    print("Tem algo errado, execute a simulação novamente.")
    prestação = 0
