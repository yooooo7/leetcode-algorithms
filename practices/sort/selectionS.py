test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def selectionSort(L: list) -> list:
    l = L.copy()
    n = len(l)

    for cur_idx in range(n):
        min_item = min(l[cur_idx:])
        min_idx = l.index(min_item, cur_idx)

        l[cur_idx], l[min_idx] = l[min_idx], l[cur_idx]
    
    return l

print(test_data)
res = selectionSort(test_data)
print(res)