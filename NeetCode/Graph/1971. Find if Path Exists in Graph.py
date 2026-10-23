class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool

        example 1:
        adj = [[1,2], [0,2], [0,1]]
        """
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        stack = [source]
        visited = [False] * n
        visited[source] = True

        while stack:
            u = stack.pop()

            if u == destination:
                return True

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        return False