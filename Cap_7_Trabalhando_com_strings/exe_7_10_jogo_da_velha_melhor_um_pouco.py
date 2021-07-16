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
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6 
---+---+---  ---+---+---
   |   |      1 | 2 | 3 

"""
linhas = []
for linha in linhas_txt.splitlines():
    linhas.append(list(linha))
# as linhas pares são as que dividem a tabela
# as linhas ímpares são as que estão vazias e onde ficarão os Xs e 0s

jogadas = 0
ganhou = False
jogador = "X"

while True:
    print(f"\nJogada {jogadas} do jogador {jogador}: ")
    for l in linhas:
        print("".join(l))
    
    if jogadas == 9:
        print("Deu velha!")
        break
    if ganhou == True:
        break

    posições_ocupadas = []
    posição = int(input(f"{jogador}, dê a posição a ser jogada: "))
    while posição <= 0 or posição >= 10:
        posição = int(input(f"Posição inválida, {jogador}! Dê a posição (1 a 9) a ser jogada: "))
    while posição in posições_ocupadas:
        posição = int(input(f"Posição já ocupada, {jogador}! Dê outra posição vazia: "))
    posições_ocupadas.append(posição)

    if posição == 1:
        linhas[5][1] = jogador
    elif posição == 2:
        linhas[5][5] = jogador
    elif posição == 3:
        linhas[5][9] = jogador
    elif posição == 4:
        linhas[3][1] = jogador
    elif posição == 5:
        linhas[3][5] = jogador
    elif posição == 6:
        linhas[3][9] = jogador
    elif posição == 7:
        linhas[1][1] = jogador
    elif posição == 8:
        linhas[1][5] = jogador
    elif posição == 9:
        linhas[1][9] = jogador


    for i in linhas:
        if (linhas[1][1] == jogador and linhas[1][5] == jogador and linhas[1][9] == jogador) or (
            linhas[3][1] == jogador and linhas[3][5] == jogador and linhas[3][9] == jogador) or (
            linhas[5][1] == jogador and linhas[5][5] == jogador and linhas[5][9] == jogador) or (
            linhas[5][1] == jogador and linhas[3][5] == jogador and linhas[1][9] == jogador) or (
            linhas[1][1] == jogador and linhas[3][5] == jogador and linhas[5][9] == jogador) or (
            linhas[1][1] == jogador and linhas[3][1] == jogador and linhas[5][1] == jogador) or (
            linhas[1][5] == jogador and linhas[3][5] == jogador and linhas[5][5] == jogador) or (
            linhas[1][9] == jogador and linhas[3][9] == jogador and linhas[5][9] == jogador):
                print(f"\n{jogador} ganhou!")
                ganhou = True
                break
    jogadas += 1

    #alternando o jogador
    if jogador == "0":
        jogador = "X"
    else:
        jogador = "0"



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