n_1 = int(input("De o primeiro numero: "))
n_2 = int(input("De o segundo numero: "))

x = n_1
r = 0
while x >= n_2:
    r = r + 1
    x = x - n_2
r = x
print(f"{n_1} % {n_2} = {r}")
