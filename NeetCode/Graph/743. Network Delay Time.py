import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        h = []
        heapq.heappush(h, (0, k))
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0

        while h:
            d, u = heapq.heappop(h)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(h, (dist[v], v))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(times, n, k))
