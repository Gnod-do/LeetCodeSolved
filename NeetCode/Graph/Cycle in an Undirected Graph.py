from collections import deque

def has_undirected_cycle(adj):
    visited = [False] * len(adj)

    for start in range(len(adj)):
        if visited[start]:
            continue

        queue = deque([(start, -1)])
        visited[start] = True

        while queue:
            u, parrent = queue.popleft()

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, u))
                elif v != parrent:
                    return True

    return False

def has_undirected_cycle_dfs(adj):
    visited = [False] * len(adj)

    def dfs(u, parrent):
        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parrent:
                return True

    for start in range(len(adj)):
        if not visited[start]:
            if dfs(start,-1):
                return True



    return False
adj3 = [
        [1],       # Đỉnh 0
        [0],       # Đỉnh 1
        [3, 4],    # Đỉnh 2
        [2, 4],    # Đỉnh 3
        [2, 3]     # Đỉnh 4
    ]

adj2 = [
        [1],    # 0 nối với 1
        [0, 2], # 1 nối với 0, 2
        [1, 3], # 2 nối với 1, 3
        [2]     # 3 nối với 2
    ]

print(has_undirected_cycle(adj2))
print(has_undirected_cycle_dfs(adj3))