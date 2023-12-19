def quicksort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[-1]
        less = [x for x in array[:-1] if x <= pivot]
        greater = [x for x in array[:-1] if x > pivot]
        return quicksort(greater) + [pivot] + quicksort(less) 
    
array_deso = [1,34,5,6,0,1123,56,7,2,4,4,57,88]
print(quicksort(array_deso))