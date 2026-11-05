import heapq

class Solution(object):
    def minTime(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        adj = [[] for _ in range(n)]
        for u,v,s,e in edges:
            adj[u].append((v,s,e))


        dist = [float('inf')] * n
        dist[0] = 0
        h = []
        heapq.heappush(h, (0,0)) # (time, node)

        while h:
            t, u = heapq.heappop(h)

            if t > dist[u]:
                continue

            if u == n - 1:
                return dist[u]

            for v,s,e in adj[u]:
                if t <= e:
                    arrival = max(s, t) + 1
                    if arrival < dist[v]:
                        dist[v] = arrival
                        heapq.heappush(h, (arrival, v))

        return -1


n = 3
edges = [[0,1,0,1],[1,2,2,5]]
sol = Solution()
print(sol.minTime(n, edges))