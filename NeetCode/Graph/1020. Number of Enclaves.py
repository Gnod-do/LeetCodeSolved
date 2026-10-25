class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 2

        while queue:
            r, c = queue.popleft()

            for i, j in directions:
                new_r, new_c = r + i, c + j

                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c))

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1

        return count
