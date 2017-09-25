def bubbleSort(List):
    flag = True
    while(flag):
        j = 0
        flag = False
        while j < (len(List) - 1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                j = j + 1
                flag = True
            else:
                j = j + 1
            print(List)
    return List


print(bubbleSort([99, 100, 3, 33, 9, 7, 10, 3]))
