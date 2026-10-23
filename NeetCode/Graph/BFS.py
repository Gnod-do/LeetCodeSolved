from collections import deque

'''
BFS chủ yếu dùng queue - FIFO
'''
def bfs(start, adj):
    n = len(adj)
    res = []
    queue = deque([start])
    visited = [False] * n

    visited[start] = True

    while queue:
        u = queue.popleft()
        res.append(u)

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return res

adj = [[1, 2], [0, 3], [0, 3], [1, 2]]
print(adj)
print(bfs(0, adj))


def bfs_f(start, adj):
    n = len(adj)

    order = []
    queue = deque([start])
    distance = [-1] * n
    distance[start] = 0
    parent = [-1] * n

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in adj[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)

    return order, distance, parent

print(bfs_f(0, adj))

def restore_path(parent, distance, target):
    if distance[target] == -1:
        return []

    path = []
    current = target

    while current != -1:
        path.append(current)
        current = parent[current]

    return path[::-1]

print(restore_path([-1, 0, 0, 1],[0, 1, 1, 2],3))
