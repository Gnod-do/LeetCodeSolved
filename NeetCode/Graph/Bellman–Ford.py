def bellmanFord(n , edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    for i in range(n-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            return None


    return dist

V = 5
edges = [[0, 1, 5], [1, 2, 1], [1, 3, 2], [2, 4, 1], [4, 3, -1]]
src = 0
print(bellmanFord(V, edges, src))