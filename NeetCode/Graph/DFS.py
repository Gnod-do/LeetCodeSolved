def dfs(start, adj):
    stack = [start]
    visited = [False] * len(adj)
    visited[start] = True

    order = []

    while stack:
        u = stack.pop()
        order.append(u)

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return order

adj = [[1, 2], [0, 3], [0, 3], [1, 2]]

print(dfs(0, adj))

'''
Độ phức tạp: O(n+m). Thường dùng cho:
1. Thành phần liên thông
2. Phát hiện chu trình
3. Backtracking
4. Topological sort
5. Các bài trên cây
'''