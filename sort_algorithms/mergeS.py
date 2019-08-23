from data import test_data

def mergeSort(L: list):
    l = L.copy()
    n = len(l)

    if n <= 1:
        return l
    
    pivot_idx = n // 2
    left_l = mergeSort(l[:pivot_idx])
    right_l = mergeSort(l[pivot_idx:])

    return merge(left_l, right_l)

def merge(left_l, right_l):
    idx_l, idx_r = 0, 0
    res_list = []

    while idx_l+1<=len(left_l) and idx_r+1<=len(right_l):
        left_item = left_l[idx_l]
        right_item = right_l[idx_r]

        if left_item < right_item:
            res_list.append(left_item)
            idx_l += 1
        else:
            res_list.append(right_item)
            idx_r += 1
    
    if idx_l+1 <= len(left_l):
        res_list += left_l[idx_l:]
    if idx_r+1 <= len(right_l):
        res_list += right_l[idx_r:]
    
    return res_list


res = mergeSort(test_data)

print(test_data)
print(res)


