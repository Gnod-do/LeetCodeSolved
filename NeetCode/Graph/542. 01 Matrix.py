from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]

        queue = deque()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and dist[new_r][new_c] == -1:
                    dist[new_r][new_c] = dist[r][c] + 1
                    queue.append((new_r, new_c))

        return dist


mat = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()
print(sol.updateMatrix(mat))