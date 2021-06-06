while True:
    print("Opções de operação (tabuadas): ")
    operação = int(input("\t1 - adição\t2 - subtração\t3 - divisão\t4 - multiplicação\t0 - sair\n"))
    if operação == 0:
        break
    else:
        numero = int(input("a tabuada é de qual numero?\n"))
        if operação == 1:
            x = 1
            while x <= 10:
                print (f"{numero} + {x} = {numero + x}")
                x += 1
        elif operação == 2:
            x = 10
            while x >= numero:
                print(f"{x} - {numero} = {x - numero}")
                x -= 1
        elif operação == 3:
            x = 10
            while x >= numero:
                print(f"{x}/{numero} = {x/numero}")
                x -= 1
        elif operação == 4:
            x = 1
            while x <= 10:
                print(f"{numero} * {x} = {numero*x}")
                x += 1

        
