testList=[1,99,34,12,41,65,75,23,3,78,24,68]

def selection_sort(L):
    suffixString = 0
    while suffixString != len(L):
        print('selection_sort: '+str(L))
        for i in range(suffixString, len(L)):
            if L[i] < L[suffixString]:
                L[suffixString],L[i] = L[i],L[suffixString]
        suffixString += 1

selection_sort(testList)
