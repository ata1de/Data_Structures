def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Escolhe o pivô (neste exemplo, o último elemento)
        pivot = arr.pop()
        # Cria duas sublistas para elementos menores e maiores que o pivô
        lowers = []
        greaters = []
        for elemento in arr:
            if elemento <= pivot:
                lowers.append(elemento)
            else:
                greaters.append(elemento)
        # Aplica recursivamente o QuickSort nas sublistas
        return quicksort(lowers) + [pivot] + quicksort(greaters)
    
array_deso = [1,34,5,6,0,1123,56,7,2,4,4,57,88]
print(quicksort(array_deso))