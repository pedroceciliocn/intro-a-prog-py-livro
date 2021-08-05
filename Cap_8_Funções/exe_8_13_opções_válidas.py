"""
Exercício 8.13 ???????????????????????????????????
Escreva uma função que receba uma string com as opções válidas
e aceitar (cada opção é uma letra). Converta as opções válidas
para letras minúsculas. Utilize input para ler uma opção,
converter o valor para letras minúsculas e verificar se a opção
é válida. Em caso de opção inválida, a função deve pedir ao
usuário que digite novamente outra opção.
"""

def valida_opções(validas):
    validas = validas.lower()
    while True:
        opção = input("Digite uma opção:").lower()
        if opção in validas:
            return opção
        print("Opção inválida, por favor escolha novamente.")

print(valida_opções('ABC'))