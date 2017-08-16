def merge_sort(a, p, r):
    if p < r:
        # 刚开始写成了
        # q = (r - p) // 2
        # maximum recursion depth exceeded in comparison错误
        q = (r + p) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    # list1: p......q
    # list2: q+1....r
    print("p=", p)
    print("q+1=", q+1)
    print(a)
    list1 = a[p : q+1]
    list2 = a[q+1 : r+1]
    index1 = 0
    index2 = 0
    key = p
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            a[key] = list1[index1]
            key = key + 1
            index1 = index1 + 1
        else:
            a[key] = list2[index2]
            key = key + 1
            index2 = index2 + 1
    if index1 == len(list1):
        while index2 < len(list2):
            a[key] = list2[index2]
            key = key + 1
            index2 = index2 + 1
    else:
        while index1 < len(list1):
            a[key] = list1[index1]
            key = key + 1
            index1 = index1 + 1

if __name__ == '__main__':
    a = [3, 1, 9, 7, 10, 5]
    merge_sort(a, 0, len(a)-1)
    print(a)
