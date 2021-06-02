quantidade= float(input("De o numero de cigarros que você costuma fumar por dia: "))
anos = float(input("Há quantos anos você fuma essa quantidade de cigarros? "))


total_de_cigarros = anos * 365 * quantidade
##minutos_perdidos = total_de_cigarros * 10
##dias_perdidos = minutos_perdidos / (24 * 60)

dias_perdidos = (total_de_cigarros * 10)/(24*60)
print(f"Você perdeu {dias_perdidos:.2f} dias da sua vida fumando. Pare de fumar!")
                     
                     
                     
