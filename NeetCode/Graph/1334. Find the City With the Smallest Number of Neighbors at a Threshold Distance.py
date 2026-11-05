class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        minNum = float('inf')
        minCity = 0
        for i in range(n):
            k = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    k += 1
            if minNum >= k:
                minNum = k
                minCity = i

        return minCity


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
solution = Solution()
print(solution.findTheCity(n, edges, distanceThreshold))