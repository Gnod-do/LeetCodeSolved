def dfs(adj, u, visited, recStack):
    if recStack[u]:
        return True

    if visited[u]:
        return False

    visited[u] = True
    recStack[u] = True

    for neighbor in adj[u]:
        if dfs(adj, neighbor, visited, recStack):
            return True

    recStack[u] = False

    return False



def isCyclic(adj):
    n = len(adj)
    visited = [False] * n
    recStack = [False] * n


    for u in range(n):
        if not visited[u] and dfs(adj, u, visited, recStack):
            return True

    return False




adj1 = [
        [1, 2],
        [2, 3],
        [3],
        []
    ]

print(isCyclic(adj1))