def heap(arr, tamanho, indice):
    maior = indice
    esquerda = 2 * indice + 1
    direita = 2 * indice + 2

    if esquerda < tamanho and arr[esquerda] < arr[maior]:
        maior = esquerda

    if direita < tamanho and arr[direita] < arr[maior]:
        maior = direita

    if maior != indice:
        arr[indice], arr[maior] = arr[maior], arr[indice]
        heap(arr, tamanho, maior)

def heap_sort(arr):
    tamanho = len(arr)

    for indice in range(tamanho // 2 - 1, -1, -1):
        heap(arr, tamanho, indice)

    for indice in range(tamanho - 1, 0, -1):
        arr[indice], arr[0] = arr[0], arr[indice]
        heap(arr, indice, 0)



# Input
init_list = input().split()
new_init_list = [int(x) for x in init_list]

# Lista onde irá ocorrer o heapsort max
lista_alterada = new_init_list.copy()
heap_sort(lista_alterada)

# Output
listaOrdenada = lista_alterada
print(f"Atenção, Grinch está indo atrás do cidadão de {listaOrdenada[0]} anos, e logo após isso ele vai atrás do cidadão de {init_list[0]} anos.")