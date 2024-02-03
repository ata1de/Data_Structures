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

def mediana(array):
    # Mediana
    if len(array) % 2 == 0:
        middle1 = (len(array) // 2) - 1
        middle2 = middle1 + 1
        mediana = float((array[middle1] + array[middle2]) / 2)
    
    else:
        mediana = array[len(array) // 2]
        

    return mediana

num_rodadas = int(input())
for rodadas in range(num_rodadas):
    array = input().split()
    array = [float(x) for x in array]
    array = quicksort(array)
    mediana_arr = mediana(array)
    media_array = sum(array)/len(array)
    array_output = [mediana_arr, media_array]
    array_final = quicksort(array_output)
    print(f'{array_final[1]:.1f}')
