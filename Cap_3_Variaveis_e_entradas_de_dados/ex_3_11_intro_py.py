preço = float(input("De o preço da mercadoria: "))
desconto = float(input("De o desconto (em %) no pagamento a vista: "))

desconto = desconto/100
preço_final = preço - preço*desconto
print(f"O valor com pagamento à vista é de R${preço_final:.2f} e o desconto foi de {desconto*100}% (ou R${preço*desconto:.2f}).")
