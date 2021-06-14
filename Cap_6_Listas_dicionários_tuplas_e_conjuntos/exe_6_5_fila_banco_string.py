# Exercício 6.5 - Simulação de uma fila de banco
último = 10
fila = list(range(1, último + 1))
sair = False

while not sair:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    x = 0

    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print(f"Fila vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último += 1
            fila.append(último)
            print(f"Cliente {último} chegou")
        elif operação[x] == "S":
            sair = True
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
