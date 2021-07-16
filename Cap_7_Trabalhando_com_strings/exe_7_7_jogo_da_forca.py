"""
Exercício 7.7 Modifique o jogo da forca (Programa 7.2) de forma a escrever a
palavra secreta caso o jogador perca.
"""
palavra = input("Digite a palavra secreta:").lower().strip() #pra padronizar a entrada
for x in range(100):
    print() # pra o outro jogador não ver a palavra digitada
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "." # 'if imediato', decide o valor a retornar, dependendo de uma condição
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou essa letra!")
        continue # pula todo o resto do codigo e volta pro começo do laço
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  0  " if erros >= 1 else "X") # mesmo tipo de if anterior
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \| "
        elif erros >= 4:
            linha2 = " \|/ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 += " /   "
        elif erros >= 6:
            linha3 += " / \ "
        print(f"X{linha3}")
        print("X\n==========")
        if erros == 6:
            print("Enforcado!")
            print(f"A palavra secreta era: {palavra}")
            break