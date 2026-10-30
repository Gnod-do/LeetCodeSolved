from collections import deque


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        def toAdj(n, dislikes):
            adj = [[] for _ in range(n + 1)]

            for u, v in dislikes:
                adj[u].append(v)
                adj[v].append(u)

            return adj

        adj = toAdj(n, dislikes)
        q = deque()
        color = [-1] * (n + 1)

        for start in range(1, n + 1):
            if color[start] != -1:
                continue

            q.append(start)

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] - 1
                        q.append(v)
                    elif color[v] == color[u]:
                        return False

        return True