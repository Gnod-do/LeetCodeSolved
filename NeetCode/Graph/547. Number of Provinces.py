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


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)
        dsu = DSU(n)

        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)

        count = sum(1 for i in range(n) if dsu.find(i) == i)
        return count

sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))