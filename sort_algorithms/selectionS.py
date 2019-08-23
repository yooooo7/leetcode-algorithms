from data import test_data

def selectionSort(L:list):
    l = L.copy()
    length = len(l)
    for i in range(length):
        smallest_item = min(l[i:])
        smallest_idx = l[i:].index(smallest_item) + i

        j = i - 1
        l[j+1], l[smallest_idx] = l[smallest_idx], l[j+1]
    
    return l

res = selectionSort(test_data)

print(test_data)
print(res)