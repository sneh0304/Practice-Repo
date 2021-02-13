def mergeSort(a):
    n = len(a)
    if n < 2:
        return a
    
    mid = int(n/2)
    
    left = a[:mid]
    right = a[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    a = merge(a, left, right)
    return a

def merge(a, l, r):
    i, j, k = 0, 0, 0
    
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    
    if i < len(l):
        a[k:] = l[i:]
    else:
        a[k:] = r[j:]
        
    return a
    
if __name__ == '__main__':
    n = int(input('Number of entries: '))
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    a = mergeSort(a)
    print(a)