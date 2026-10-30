from collections import deque


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u,v in edges:
            visited = [False] * (n + 1)
            visited[u] = True
            queue = deque([u])

            while queue:
                node = queue.popleft()

                if node == v:
                    return [u,v]

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            adj[u].append(v)
            adj[v].append(u)

        return []


edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
solution = Solution()
print(solution.findRedundantConnection(edges))