# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda
estoque = {"tomate": [1000, 2.30],
           "alface": [ 500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [ 100, 1.50],
}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação #desempacotamento: 1º elemento de operação atribuído a produto e o 2º a quantidade 
    preço = estoque[produto][1] #o segundo elem da lista armazena o preço
    custo = preço*quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade #subtraindo a qtd vendida
    total += custo
print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items(): #items é um gerador que retorna uma tupla contendo a chave e o valor de cada item do dic
    print(f"Descrição: {chave}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: {dados[1]:6.2f}\n")

"""
for operação in venda:
    produto, quantidade = operação
seria equivalente a:
produto = operação[0]
quantidade = operação[1]
"""