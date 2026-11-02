import heapq

def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0,start))
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))

    return dist
adj = [
    [[1, 4], [2, 8]],
    [[0, 4], [4, 6], [2, 3]],
    [[0, 8], [3, 2], [1, 3]],
    [[2, 2], [4, 10]],
    [[1, 6], [3, 10]]
]
src = 0
print(dijkstra(adj, src))