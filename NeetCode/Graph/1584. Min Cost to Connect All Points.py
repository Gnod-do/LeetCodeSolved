import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                w = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([j, w])

        count = 0
        total = 0
        heap = [(0, 0)]
        visited = [False] * n

        while heap and count < n:
            w, u = heapq.heappop(heap)

            if visited[u]:
                continue

            count += 1
            total += w
            visited[u] = True

            for v, w2 in adj[u]:
                if not visited[v]:
                    heapq.heappush(heap, (w2, v))

        return total

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))