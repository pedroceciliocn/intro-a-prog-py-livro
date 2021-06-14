# Exercício 6.6 - Simulação de duas filas de banco
último_A = 10
último_B = 10
fila_A = list(range(1, último_A + 1))
fila_B = list(range(1, último_B + 1))
sair = False
atendido_A = []
atendido_B = []
while not sair:
    print(f"\nExistem {len(fila_A)} clientes na fila A")
    print(f"\nExistem {len(fila_B)} clientes na fila B")
    print(f"Fila A atual: {fila_A}")
    print(f"Fila B atual: {fila_B}")
    print("Digite F para adicionar um cliente ao fim da fila A,")
    print("Digite G para adicionar um cliente ao fim da fila B,")
    print("ou A para realizar um atendimento na fila A,")
    print("ou B para realizar um atendimento na fila B. S para sair.")
    operação = input("Operação (A, B, F, G ou S):")
    x = 0

    while x < len(operação):
        if operação[x] == "A":
            if len(fila_A) > 0:
                atendido_A = fila_A.pop(0)
                print(f"Cliente {atendido_A} da fila A atendido")
            else:
                print(f"Fila A vazia! Ninguém para atender.")
        if operação[x] == "B":
            if len(fila_B) > 0:
                atendido_B = fila_B.pop(0)
                print(f"Cliente {atendido_B} da fila B atendido")
            else:
                print(f"Fila B vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último_A += 1
            fila_A.append(último_A)
            print(f"Cliente {último_A} chegou na fila A")
        elif operação[x] == "G":
            último_B += 1
            fila_B.append(último_B)
            print(f"Cliente {último_B} chegou na fila B")
        elif operação[x] == "S":
            sair = True
        else:
            print("Operação inválida! Digite apenas A, B, F, G ou S!")
        x += 1
