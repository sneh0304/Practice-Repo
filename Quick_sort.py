def quickSort(a, start, end):
    if start < end:
        pIndex = partition(a, start, end)
        quickSort(a, start, pIndex-1)
        quickSort(a, pIndex+1, end)

def partition(a, l, r):
    key = a[r]
    pIndex = l
    for i in range(l, r):
        if a[i] <= key:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[r], a[pIndex] = a[pIndex], key
    
    return pIndex
    
if __name__ == '__main__':
    n = int(input('Number of entries: '))
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    quickSort(a, 0, len(a)-1)
    print(a)
