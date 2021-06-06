total = 0
while True:
    codigo = int(input("Digite o codigo do produto (ou 0 para sair): "))
    preço = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preço = 0.50
    elif codigo == 2:
        preço = 1.00
    elif codigo == 3:
        preço = 4.00
    elif codigo == 5:
        preço = 7.00
    elif codigo == 9:
        preço = 8.00
    else:
        print("Código inválido, escolha 1, 2, 3, 5 ou 9.")
    if preço != 0:
        quantidade = int(input("Digite a quantidade comprada: "))
        total = total + (preço * quantidade)
print(f"O total a ser pago é de R${total:.2f}")
