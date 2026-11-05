import heapq

def shortestPath(a, b, adj):

    n = len(adj)
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    dist[a][0] = 0
    h = []
    heapq.heappush(h, (0, a, 0)) # weight, node, usedCurve


    while h:
        d, u, used = heapq.heappop(h)

        if d != dist[u][used]:
            continue

        for v, w1, w2 in adj[u]:
            # Take straight edge
            if dist[v][used] > d + w1:
                dist[v][used] = d + w1
                heapq.heappush(h, (d + w1, v, used))

            # Use curved edge if not used before
            if used == 0:
                if dist[v][1] > d + w2:
                    dist[v][1] = d + w2
                    heapq.heappush(h, (d + w2, v, 1))

    ans = min(dist[b][0], dist[b][1])
    return ans if ans != float('inf') else -1





a = 1
b = 3
adj = [[[1, 1, 4], [2, 2, 4], [3, 3, 1]], [[0, 1, 4], [3, 6, 5]], [[0, 2, 4]],[[0, 3, 1], [1, 6, 5]]]
print(shortestPath(a,b,adj))