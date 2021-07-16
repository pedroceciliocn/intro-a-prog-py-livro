# Programa 7.1 - Pesquisa de todas as ocorrências
s = "um tigre, dois tigres, três tigres"
p = 0
while p > -1:
    p = s.find("tigre", p) #acha a string inteira e diz a posição, o p é o início. Se receber -1, é pq não achou
    if p >= 0:
        print(f"Posição: {p}")
        p += 1
