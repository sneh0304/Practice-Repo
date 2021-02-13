class UF:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
        self.components = n
        
    def find(self, node):
        root = node
        while root != self.parent[root]:
            root = self.parent[root]
        
        while node != self.parent[node]:
            node, self.parent[node] = self.parent[node], root
            
        return root
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        if self.size[parent_u] > self.size[parent_v]:
            self.parent[v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        
        self.components -= 1
        
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    
    uf = UF(n)
    for u, v in edges:
        if not uf.isConnected(u, v):
            uf.union(u, v)
    
    return uf.components == 1
    
    
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(validTree(n, edges)
  
n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(validTree(n, edges)