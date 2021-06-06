s = 0
q = 0
while True:
    v = int(input("Digite um numero a somar ou 0 para sair:"))
    if v == 0:
        break
    s += v
    q += 1
print(f"A quantidade de numeros digitados foi: {q}")
print(f"A soma foi {s} e a média {s/q}.")
