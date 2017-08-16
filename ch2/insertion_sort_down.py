def insertion_sort_down(a):
    length = len(a)
    for j in range(1, length):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key

if __name__ == '__main__':
    a = [9, 3, 7, 11, 5]
    insertion_sort_down(a)
    print(a)