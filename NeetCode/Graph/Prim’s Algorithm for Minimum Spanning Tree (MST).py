import heapq

from nbformat import v2


def primMST(adj, V):
    visited = [False] * V
    heap = [(0,0)]
    total = 0
    count = 0

    while heap and count < V:
        w, u = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        total += w
        count += 1

        for v, w2 in adj[u]:
            if not visited[v]:
                heapq.heappush(heap, (w2, v))

    return total
