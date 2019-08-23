test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def bubbleSort(L: list) -> list:
    l = L.copy()
    n = len(l)

    exchange = False

    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                exchange = True
        if not exchange:
            break
    
    return l

print(test_data)
res = bubbleSort(test_data)
print(res)