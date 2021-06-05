n = int(input("Tabuada de:"))
x = int(input("A partir de:"))
fim = int(input("Até o numero:"))
while x <= fim:
    print(f"{x}x{n} = {n * x}") #seria bom limitar o n
    x = x + 1
