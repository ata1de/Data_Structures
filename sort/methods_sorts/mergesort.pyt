def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0

        # Conferir se o index passou por todos os elementos das duas listas
        while i < len(lefthalf) and j < len(righthalf):
            # Se o topo de alguma lista for menor que o outro, a lista principal será mudada
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        # Verificação se o index esqueceu de passar em alguma lista
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1

lista = [12, 11, 13, 5, 6, 7]
merge_sort(lista)