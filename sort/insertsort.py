def insertion_sort(arr):
    # Percorre toda a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        # Move os elementos da lista que são maiores que a chave para uma posição à frente
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = chave

# Exemplo de uso
lista = [12, 11, 13, 5, 6]
insertion_sort(lista)

print("Lista ordenada:", lista)