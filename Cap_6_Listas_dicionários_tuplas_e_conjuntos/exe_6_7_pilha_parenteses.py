expressão = input("Digite a sequência de parênteses a ser validada:")
x=0
pilha = []
while x < len(expressão):
    if(expressão[x] == "("):
        pilha.append("(")
    if(expressão[x] == ")"):
        if(len(pilha)>0):
            del pilha[-1]
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x=x+1
if(len(pilha) == 0):
    print("OK")
else:
    print("Erro")