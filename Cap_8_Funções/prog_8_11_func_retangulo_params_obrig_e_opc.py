# Programa 8.11 - Função retângulo com parâmetros obrigatórios e opcionais
def retângulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retângulo(3, 4)

retângulo(altura=4, largura=3)

retângulo(caractere="-", altura=4, largura=3)

#chamadas inválidas, pois é obrigatório que se nomeie o restante dos parametros no caso de um ser nomeado
# retângulo(largura=3, 4)
# retângulo(largura=3, altura=4, "*")