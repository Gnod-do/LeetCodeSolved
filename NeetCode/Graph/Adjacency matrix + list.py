n = 4

edges = [(0,1), (0,2), (1,3), (2,3)]

matrix = [[0] * n for _ in range(n)]

for u,v in edges:
    matrix[u][v] = 1

print(matrix)

adj = [[] for _ in range(n)]

for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

print(adj)


def weigted_edges():
    n = 4
    weigted_edges = [
        (0,1,5),
        (0,2,2),
        (1,3,4)
    ]

    adj = [[] for _ in range(n)]

    for u,v, weight in weigted_edges:
        adj[u].append((v,weight))
        adj[v].append((u,weight))
    print(adj)

weigted_edges()

