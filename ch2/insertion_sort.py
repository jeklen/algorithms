def insertion_sort(a):
    length = len(a)
    for j in range(1, length):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key

a = [2, 1, 9, 6, 5]
insertion_sort(a)
print(a)
