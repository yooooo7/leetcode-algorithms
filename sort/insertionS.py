test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def insertionSort(L: list) -> list:
    l = L.copy()
    n = len(l)

    for i in range(1, n):
        temp = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > temp:
                l[j+1] = l[j]
                j -= 1
            else: 
                break
        
        l[j+1] = temp
    
    return l

print(test_data)
res = insertionSort(test_data)
print(res)