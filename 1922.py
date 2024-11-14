class graph():

    def __init__(self,v):
        self.edge = []
        self.v = v
        self.parent = list(range(v+1))

    def add(self, a, b, w):
        self.edge.append((w,a,b))

    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            return self.find(self.parent[v])
        
    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)

        if p1 < p2:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2

    def kruskal(self):
        sum = 0
        self.edge.sort()
        for w,a,b in self.edge:
            if self.find(a) != self.find(b):
                self.union(a,b)
                sum += w
        
        return sum
    

n = int(input())

g = graph(n)

for i in range(int(input())):
    a,b,w = map(int , input().split())
    g.add(a,b,w)

print(g.kruskal())

