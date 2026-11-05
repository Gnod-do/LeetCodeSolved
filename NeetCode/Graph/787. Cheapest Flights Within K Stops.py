class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k+1):
            tmp = dist.copy()
            for u,v,w in flights:
                if dist[u] != float('inf') and tmp[v] > dist[u] + w:
                    tmp[v] = dist[u] + w
            dist = tmp

        return dist[dst] if dist[dst] != float('inf') else -1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

solution = Solution()
print(solution.findCheapestPrice(n, flights, src, dst, k))