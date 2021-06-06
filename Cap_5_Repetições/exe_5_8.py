##n_1 = int(input("Digite o primeiro numero:"))
##n = n_1
##n_2 = int(input("Digite o segundo numero:"))
##resultado = 0
##if n_1 < n_2:
##    while n <= n_2:
##        resultado = n + n_2 
##        n = n + 1
##    print(f"{n_1}x{n_2} = {resultado}")
##
##if n_1 > n_2:
##    n_1,n_2 = n_2,n_1
##    while n <= n_2:
##        resultado = n + n_2 
##        n = n + 1
##    print(f"{n_2}x{n_1} = {resultado}")

# pessima solução

n_1 = int(input("Digite o primeiro numero:"))
n_2 = int(input("Digite o segundo numero:"))
contador = 1
resultado = 0

while contador <= n_2: # o segundo numero é usado com o 'fim' dos outros exemplos
    resultado = resultado + n_1
    contador = contador + 1
print(f"{n_1}x{n_2} = {resultado}")

#na primeira tentativa de fazer esse programa, tive problemas no raciocinio
#e so funcionava se o primeiro numero fosse o menor (o segundo seria a referencia
#pra fazer as somas repetidas, mas burrei era so usar o segundo como 'base',
#independente de ele ser maior ou menor que o primeiro numero.
