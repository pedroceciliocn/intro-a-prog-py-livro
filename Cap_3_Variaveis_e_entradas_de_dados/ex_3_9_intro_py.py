dias = int(input("De o numero de dias: "))
horas = int(input("De o numero de horas: "))
minutos = int(input("De o numero de minutos: "))
segundos = int(input("De o numero de segundos: "))

total = (dias *  60**2 * 24) + (horas * 60**2) + (minutos * 60) + segundos
print(f"O numero total de segundos é de {total}.")
