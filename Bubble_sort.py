def bubbleSort(a):
    for i in range(len(a)):
        flag = True
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = False
        if flag:
            break
    return a
    
if __name__ == '__main__':
    n = int(input('Number of entries: '))
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    a = bubbleSort(a)
    print(a)