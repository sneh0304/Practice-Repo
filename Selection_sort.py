def selectionSort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        
    return a
    
if __name__ == '__main__':
    n = int(input('Number of entries: '))
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    a = selectionSort(a)
    print(a)