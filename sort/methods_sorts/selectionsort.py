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

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)
    