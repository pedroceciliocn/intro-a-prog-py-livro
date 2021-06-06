while True:
    print("Opções de operação (tabuadas): ")
    operação = int(input("\t1 - adição\t2 - subtração\t3 - divisão\t4 - multiplicação\t0 - sair\n"))
    if operação == 0:
        break
    elif operação == 1 or operação == 2 or operação == 3 or operação == 4:
        numero = int(input("a tabuada é de qual numero?\n"))
        x = 1
        while x <= 10:
            if operação == 1:
                print (f"{numero} + {x} = {numero + x}")
            elif operação == 2:
                print(f"{x} - {numero} = {x - numero}")
            elif operação == 3:
                print(f"{x}/{numero} = {x/numero}")
            elif operação == 4:
                print(f"{numero} * {x} = {numero*x}")
            x += 1
    else:
        print("Operação inválida!")
        
