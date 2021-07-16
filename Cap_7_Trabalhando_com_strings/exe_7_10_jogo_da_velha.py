"""
Exercício 7.10 Escreva um jogo da velha para dois jogadores. O jogo deve perguntar
onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
posição está livre. Verifique também quando um jogador venceu a partida.
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento
é outra lista, também com três elementos.
Exemplo do jogo:

     X | 0 |       
    ---+---+---
       | X | X
    ---+---+---
       |   | 0 
Em que cada posição pode ser vista como um número. Confira a seguir um exemplo
das posições mapeadas para a mesma posição de seu teclado numérico.
     7 | 8 | 9       
    ---+---+---
     4 | 5 | 6
    ---+---+---
     1 | 2 | 3  
"""

#criação da estrutura do jogo
linhas_txt = """
   |   |       
---+---+---
   |   |  
---+---+---
   |   |   

"""
linhas = []
for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

# as linhas pares são as que dividem a tabela
# as linhas ímpares são as que estão vazias e onde ficarão os Xs e 0s


jogadas = 0
ganhou = False

while True:
    print(f"\nJogada {jogadas}: ")
    for l in linhas:
        print("".join(l))
    
    if jogadas == 9:
        print("Deu velha!")
        break
    if ganhou == True:
        break

    jogador = int(input("Dê o jogador (1 ou 2): ")) #fazer algo pra alternar os jogadores
    while jogador != 1 and jogador != 2:
        jogador = int(input("Dê o jogador (1 ou 2): "))

    posições_ocupadas = []
    posição = int(input("Dê a posição a ser jogada: "))
    while posição <= 0 or posição >= 10:
        posição = int(input("Posição inválida! Dê a posição (1 a 9) a ser jogada: "))
    while posição in posições_ocupadas:
        posição = int(input("Posição já ocupada! Dê outra posição vazia: "))
    posições_ocupadas.append(posição)


    if jogador == 1:
        if posição == 1:
            linhas[5][1] = "0"
        elif posição == 2:
            linhas[5][5] = "0"
        elif posição == 3:
            linhas[5][9] = "0"
        elif posição == 4:
            linhas[3][1] = "0"
        elif posição == 5:
            linhas[3][5] = "0"
        elif posição == 6:
            linhas[3][9] = "0"
        elif posição == 7:
            linhas[1][1] = "0"
        elif posição == 8:
            linhas[1][5] = "0"
        elif posição == 9:
            linhas[1][9] = "0"

    if jogador == 2:
        if posição == 1:
            linhas[5][1] = "X"
        elif posição == 2:
            linhas[5][5] = "X"
        elif posição == 3:
            linhas[5][9] = "X"
        elif posição == 4:
            linhas[3][1] = "X"
        elif posição == 5:
            linhas[3][5] = "X"
        elif posição == 6:
            linhas[3][9] = "X"
        elif posição == 7:
            linhas[1][1] = "X"
        elif posição == 8:
            linhas[1][5] = "X"
        elif posição == 9:
            linhas[1][9] = "X"
    jogadas += 1

    for i in linhas:
        if (linhas[1][1] == "X" and linhas[1][5] == "X" and linhas[1][9] == "X") or (
            linhas[3][1] == "X" and linhas[3][5] == "X" and linhas[3][9] == "X") or (
            linhas[5][1] == "X" and linhas[5][5] == "X" and linhas[5][9] == "X") or (
            linhas[5][1] == "X" and linhas[3][5] == "X" and linhas[1][9] == "X") or (
            linhas[1][1] == "X" and linhas[3][5] == "X" and linhas[5][9] == "X") or (
            linhas[1][1] == "X" and linhas[3][1] == "X" and linhas[5][1] == "X") or (
            linhas[1][5] == "X" and linhas[3][5] == "X" and linhas[5][5] == "X") or (
            linhas[1][9] == "X" and linhas[3][9] == "X" and linhas[5][9] == "X"):
                print("\nX ganhou!")
                ganhou = True
                break
        elif (linhas[1][1] == "0" and linhas[1][5] == "0" and linhas[1][9] == "0") or (
            linhas[3][1] == "0" and linhas[3][5] == "0" and linhas[3][9] == "0") or (
            linhas[5][1] == "0" and linhas[5][5] == "0" and linhas[5][9] == "0") or (
            linhas[5][1] == "0" and linhas[3][5] == "0" and linhas[1][9] == "0") or (
            linhas[1][1] == "0" and linhas[3][5] == "0" and linhas[5][9] == "0") or (
            linhas[1][1] == "0" and linhas[3][1] == "0" and linhas[5][1] == "0") or (
            linhas[1][5] == "0" and linhas[3][5] == "0" and linhas[5][5] == "0") or (
            linhas[1][9] == "0" and linhas[3][9] == "0" and linhas[5][9] == "0"):
                print("\n0 ganhou!")
                ganhou = True
                break


#(linhas[1][1]) onde fica o elemento 7
#(linhas[1][5]) onde fica o elemento 8
#(linhas[1][9]) onde fica o elemento 9
#-------------------------------------
#(linhas[3][1]) onde fica o elemento 4
#(linhas[3][5]) onde fica o elemento 5
#(linhas[3][9]) onde fica o elemento 6
#-------------------------------------
#(linhas[5][1]) onde fica o elemento 1
#(linhas[5][5]) onde fica o elemento 2
#(linhas[5][9]) onde fica o elemento 3