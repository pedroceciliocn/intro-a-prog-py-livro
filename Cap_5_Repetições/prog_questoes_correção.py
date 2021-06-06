##pontos = 0
##questão = 1
##while questão <= 3:
##    resposta = input(f"Resposta da questão {questão}: ").lower() #usando a função lower pra converter tudo pra minusculo
##    if questão == 1 and resposta == "b":
##        pontos += 1
##    if questão == 2 and resposta == "a":
##        pontos += 1
##    if questão == 3 and resposta == "d":
##        pontos += 1
##    questão += 1
##print(f"O aluno fez {pontos} ponto(s).")


pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and resposta == "b" or resposta == "B": #versão sugerida pelo livro
        pontos += 1
    if questão == 2 and resposta == "a" or resposta == "A":
        pontos += 1
    if questão == 3 and resposta == "d" or resposta == "D":
        pontos += 1
    questão += 1
print(f"O aluno fez {pontos} ponto(s).")
