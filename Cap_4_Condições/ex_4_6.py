distancia = float(input("De a distancia que pretende percorrer (em km): "))


preço = 0
if distancia <= 200:
    preço = 0.50*distancia
else:
    preço = 0.45*distancia
print(f"O preço da passagem foi de R${preço:.2f}.")    
