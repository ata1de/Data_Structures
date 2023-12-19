def insertion_sort(array):
    for i in range(1, len(array)):
        chave = array[i]
        pointer = i - 1

        while pointer >= 0 and chave < array[pointer]:
            array[pointer + 1] = array[pointer]
            pointer -= 1

        array[pointer + 1] = chave

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
    

def merge_sort(array):
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0, 0,0

        # Conferir se o index passou por todos os elementos das duas listas
        while i < len(lefthalf) and j < len(righthalf):
            # Se o topo de alguma lista for menor que o outro, a lista principal será mudada
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i+=1
            else:
                array[k]=righthalf[j]
                j+=1
            k+=1

        # Verificação se o index esqueceu de passar em alguma lista
        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j+=1
            k+=1

def selection_sort(array):
    n = len(array)
    num_sort = 0
    i = 0
    while(num_sort < n):
        minimo, index_minimo = get_minimum(i, array)
        array[i], array[index_minimo] = minimo, array[i]
        i+=1
        num_sort+=1 
        
def get_minimum(start, array):
    #Achando o minimo da lista
    minimo = array[start]
    n = len(array)
    index_minimo = start
    for i in range(start,n):
        if array[i] < minimo:
            minimo = array[i]
            index_minimo = i

    return minimo, index_minimo

def shellSort(array):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            chave = array[i]
            j = i
            
            while j >= interval and array[j - interval] > chave:
                array[j] = array[j - interval]
                j -= interval

            array[j] = chave
        interval //= 2


array_inital = input().split(', ')
array = list(map(int, array_inital))
algorithm = input()
doblo = input()

if algorithm == "Shell Sort":
    shellSort(array)
elif algorithm == "Selection Sort":
    selection_sort(array)
elif algorithm == "Insertion Sort":
    insertion_sort(array)
elif algorithm == "Merge Sort":
    merge_sort(array)
elif algorithm == "Quick Sort":
    array = quicksort(array)

if doblo == 'dobre!':
    double_list = [x * 2 for x in array]
    print(double_list)
else:
    print(array)