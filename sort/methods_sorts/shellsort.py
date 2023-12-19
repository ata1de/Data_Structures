# Shell sort in python
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
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)