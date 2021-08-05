"""
Exercício 8.12 Escreva uma função que receba uma string e uma lista. A função
deve comparar a string passada com os elementos da lista, também passada como
parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso,
caso contrário.
"""
def string_na_lista(string, lista):
    if string in lista:
        return True
    else:
        return False

print(string_na_lista("plmds", ['ava', 'vixe', 'mds', 'god', 'plmds']))