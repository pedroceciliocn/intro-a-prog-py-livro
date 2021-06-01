materia1 = float(input("Digite sua nota na primeira materia: "))
materia2 = float(input("Digite sua nota na segunda materia: "))
materia3 = float(input("Digite sua nota na terceira materia: "))

if materia1 >= 7.0 and materia2 >= 7.0 and materia3 >= 7.0:
    aprovado = True
else:
    aprovado = False
print(f"It's {aprovado} that you are approved.")
