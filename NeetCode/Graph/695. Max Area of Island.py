class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r_start, c_start):
            area = 1
            stack = [(r_start, c_start)]

            grid[r_start][c_start] = 0

            while stack:
                r, c = stack.pop()

                for i, j in directions:
                    r_new, c_new = r + i, c + j

                    if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new] == 1:
                        area += 1
                        grid[r_new][c_new] = 0
                        stack.append((r_new, c_new))

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)

        return max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()

print(sol.maxAreaOfIsland(grid))