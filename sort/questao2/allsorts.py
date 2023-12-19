def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        pointer = i - 1

        while pointer >= 0 and chave < lista[pointer]:
            lista[pointer + 1] = lista[pointer]
            pointer -= 1

        lista[pointer + 1] = chave

def quicksort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[-1]
        less = [x for x in array[:-1] if x <= pivot]
        greater = [x for x in array[:-1] if x > pivot]
        return quicksort(greater) + [pivot] + quicksort(less) 