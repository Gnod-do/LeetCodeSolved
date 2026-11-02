import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        prob = [0.0] * n            # ← khởi tạo "tệ nhất" = 0
        prob[start_node] = 1.0           # ← nguồn = 1
        h = [(-1.0, start_node)]         # max-heap: đẩy -1.0

        while h:
            p, u = heapq.heappop(h)
            p = -p                  # đổi dấu lại thành xác suất thật

            if p < prob[u]:         # ← lazy deletion (đảo dấu so với min)
                continue

            if u == end_node:
                return p

            for v, w in adj[u]:
                if p * w > prob[v]:         # ← tìm LỚN hơn
                    prob[v] = p * w
                    heapq.heappush(h, (-(p * w), v))

        return 0.0



n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

sol = Solution()
print(sol.maxProbability(n, edges, succProb, start, end))