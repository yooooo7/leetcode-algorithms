test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def bubbleSort(L: list) -> list:
    l = L.copy()
    n = len(l)

    for i in range(n):
        ifExchange = False
        for j in range(0, n - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                ifExchange = True
        
        if not ifExchange:
            break
    
    return l

print(test_data)
res = bubbleSort(test_data)
print(res)