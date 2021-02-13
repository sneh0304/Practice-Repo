def insertionSort(a):
    for i in range(1, len(a)):
        value = a[i]
        hole = i
        while hole > 0 and a[hole-1] > value:
            a[hole] = a[hole-1]
            hole -= 1
        
        a[hole] = value
    return a
    
if __name__ == '__main__':
    n = int(input('Number of entries: '))
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    a = insertionSort(a)
    print(a)