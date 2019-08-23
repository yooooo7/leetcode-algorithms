from data import test_data

def insertionSort(L:list):
    l = L.copy()
    length = len(l)
    
    for i in range(1, length):
        item = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > item:
                l[j+1] = l[j]
                j -= 1
            else:
                break
        l[j+1] = item

    return l

res = insertionSort(test_data)

print(test_data)
print(res)