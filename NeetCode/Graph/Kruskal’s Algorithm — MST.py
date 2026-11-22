class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[ry] == self.rank[rx]:
            self.rank[rx] += 1

        return True

def kruskalMST(V, edges):
    edges.sort()
    dsu = DSU(V)
    total = 0
    count = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            count += 1
            total += w
            if count == V - 1:
                break

    return total

V = 4
edges = [[10, 0, 1], [15, 1, 3], [4, 2, 3], [6, 2, 0], [5, 0, 3]]
print(kruskalMST(V, edges))