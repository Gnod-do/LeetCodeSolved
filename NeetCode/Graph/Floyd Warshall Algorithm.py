def floyd_warshall(dist):
    V = len(dist)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


dist = [[0, 4, float('inf'), 5, float('inf')],
        [float('inf'), 0, 1, float('inf'), 6],
        [2, float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 1, 0, 2],
        [1, float('inf'), float('inf'), 4, 0]]

print(floyd_warshall(dist))