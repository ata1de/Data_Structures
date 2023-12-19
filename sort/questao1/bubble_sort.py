def extrair_numero(string):
    num = ""
    for letra in string:
        if letra.isdigit():
            num += letra
    return int(num) if num else 0

def bubble_sort(lista, condition=False):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            # Essa condição é para verificar se vamos fazer o bubble sort nas praças ou nos nomes
            if condition:
                # Extraio os números e depois comparo eles para ordená-los
                num1 = extrair_numero(lista[i])
                num2 = extrair_numero(lista[i+1])

                if num1 > num2:
                    lista[i],lista[i+1] = lista[i+1],lista[i]
            else:
                if lista[i] > lista[i+1]:
                    lista[i],lista[i+1] = lista[i+1],lista[i]

manager = {}
list_squares = []
squares = int(input())
for sq in range(squares):
    # Coletando os inputs e transformando a string das crianças em uma lista
    square, children = input().split(': ')

    # Sorteando as crianças, jutando em uma str e depois adicionando no dicionário
    childrens = children.split()
    bubble_sort(childrens)
    str_childrens = ' '.join(childrens)
    manager[square] = str_childrens

    # Adicionar os squares em uma lista para depois ordena-la
    list_squares.append(square)

# Ordenando as praças e depois printando o output
bubble_sort(list_squares, True)
for square in list_squares:
    print(f'{square}: {manager[square]}')

