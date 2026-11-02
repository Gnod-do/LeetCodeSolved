from collections import deque

def topoSort(adj):
    res = []
    queue = deque()

    indegree = [0] * len(adj)

    for u in range(len(adj)):
        for v in adj[u]:
            indegree[v] += 1

    for u in range(len(adj)):
        if indegree[u] == 0:
            queue.append(u)

    while queue:
        u = queue.popleft()
        res.append(u)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)


    return res


adj = [[1], [2], [], [2, 4], []]

print(topoSort(adj))

'''
Nếu dùng Kahn' Algorithm thì dưới đây là các bước cho bài này:
1. Tính in-degree của từng node trong đồ thị
2. Add node có in-degree = 0 vào queue
3. Duyệt queue -> bfs qua các nốt lân cận -> tính lại in-degree của các node sau khi pop(top). Add
vào queue nếu node nào có in-degree = 0
'''