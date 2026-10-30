from collections import deque

def is_bipartite(adj):
    color = [-1] * len(adj)
    queue = deque()

    for start in range(len(adj)):
        if color[start] != -1:
            continue

        queue.append(start)

        while queue:
            u = queue.popleft()

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] - 1
                    queue.append(v)
                elif color[v] == color[u]:
                    return False

    return True


adj = [[1,4], [2,0], [3,1], [4,2], [0]]
print(is_bipartite(adj))