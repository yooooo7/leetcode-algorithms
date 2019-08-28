test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def insertionSort(L: list) -> list:
    l = L.copy()
    n = len(l)

    sorted_idx = 0

    while sorted_idx < n - 1:
        cur_item = l[sorted_idx + 1]
        insert_idx = sorted_idx + 1
        
        while insert_idx > 0:
            if l[insert_idx - 1] > cur_item:
                l[insert_idx] = l[insert_idx - 1]
                insert_idx -= 1
            else:
                break
        
        l[insert_idx] = cur_item
        sorted_idx += 1
    
    return l


print(test_data)
res = insertionSort(test_data)
print(res)