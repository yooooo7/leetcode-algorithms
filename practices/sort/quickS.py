test_data = [5, 4, 123, 43294, 573, 5, 58, 984, 58, 48, 48, 249]

def quickSort(L: list) -> int:
    l = L.copy()
    n = len(l)

    left, right = 0, n - 1

    qS(l, left, right)

    return l

def qS(l, left, right):
    if left >= right: return

    pivot_idx = partation(l, left, right)
    
    qS(l, left, pivot_idx - 1)
    qS(l, pivot_idx + 1, right)

def partation(l, left, right):
    pivot = l[right]
    
    i = left

    for j in range(left, right):
        if l[j] < pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    
    l[i], l[right] = l[right], l[i]

    return i

res = quickSort(test_data)
print(test_data)
print(res)