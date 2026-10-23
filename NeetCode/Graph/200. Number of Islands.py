class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0

        def dfs(r_start, c_start):
            stack = [(r_start, c_start)]
            grid[r_start][c_start] = '0'

            while stack:
                r, c = stack.pop()

                for i,j in directions:
                    nr, nc = r + i, c + j

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        stack.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)

        return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))