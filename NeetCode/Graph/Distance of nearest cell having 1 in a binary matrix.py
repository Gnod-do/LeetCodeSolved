from collections import deque

def nearest(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]

    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dist[i][j] = 0
                queue.append((i,j))
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < rows and 0 <= new_c < cols and dist[new_r][new_c] == -1:
                dist[new_r][new_c] = dist[r][c] + 1
                queue.append((new_r, new_c))

    return dist




grid = [[0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]]

print(nearest(grid))