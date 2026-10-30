from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [-1] * len(graph)
        queue = deque()

        for start in range(len(graph)):
            if color[start] != -1:
                continue

            queue.append(start)

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = color[u] - 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False

        return True