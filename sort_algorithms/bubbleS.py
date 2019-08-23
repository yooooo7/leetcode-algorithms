from data import test_data

def bubbleSort(List: list):
    l = List.copy()

    if len(l) <= 1:
        return l

    for i in range(len(l)):
        ifExchange = False
        # 一次冒泡过程
        for j in range(len(l)-i-1):
            first = l[j]
            second = l[j+1]
            if first > second:
                l[j], l[j+1] = l[j+1], l[j]
                ifExchange = True
        
        if not ifExchange:
            break
    
    return l

res = bubbleSort(test_data)

print(test_data)
print(res)