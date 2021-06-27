# Programa 6.13 - Controle da utilização de salas de um cinema
lugares_vagos = [10, 2, 1, 3, 0] #numero de lugares vagos por cada sala (de 1 a 5)

while sala != 0:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilização das salas")
for x, l in enumerate(lugares_vagos):
    print(f"Sala {x + 1} - {l} lugar(es) vazio(s)")