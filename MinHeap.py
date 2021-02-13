import sys

class minHeap():
    def __init__(self, arr, n):
        self.harr = arr
        self.heapSize = n
        i = (self.heapSize // 2) - 1
        while i >= 0:
            self.heapify(i)
            i -= 1
    
    def left(self, i):
        return (i * 2) + 1
    
    def right(self, i):
        return (i * 2) + 2
    
    def parent(self, i):
        return (i - 1) // 2
    
    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heapSize and self.harr[l] < self.harr[smallest]:
            smallest = l
        if r < self.heapSize and self.harr[r] < self.harr[smallest]:
            smallest = r
        if smallest != i:
            self.harr[smallest], self.harr[i] = self.harr[i], self.harr[smallest]
            self.heapify(smallest)
    
    def extractMin(self):
        if self.heapSize == 0:
            return sys.maxsize
        
        min = self.harr[0]
        if self.heapSize > 1:
            self.harr[0] = self.harr[self.heapSize - 1]
            self.heapSize -= 1
            self.heapify(0)
        
        return min
    
    def getMin(self):
        return self.harr[0]
    
    def heapSort(self):
        n = self.heapSize
        while n > 0:
            res = self.extractMin()
            self.harr[n - 1] = res
            n -= 1
    
if __name__ == '__main__':
    a = [12, 11, 13, 5, 6, 7, 1, 10, 100, 8]
    print('Initial array: ', a)
    minheap = minHeap(a, len(a))
    print('After heapify, array: ', a)
    print('Minimum element: ', minheap.getMin())
    minheap.heapSort()
    print('After heap sort, array: ', a)
    