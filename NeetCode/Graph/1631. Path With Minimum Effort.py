import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(heights), len(heights[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        h = []
        heapq.heappush(h, (0,0,0)) # effort, row, col

        while h:
            e,r,c = heapq.heappop(h)

            if e > effort[r][c]:
                continue

            if (r,c) == (rows-1,cols-1):
                return e

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    diff = abs(heights[new_r][new_c] - heights[r][c])
                    new_effort = max(e, diff)
                    if new_effort < effort[new_r][new_c]:
                        effort[new_r][new_c] = new_effort
                        heapq.heappush(h, (new_effort, new_r, new_c))

        return 0


heights = [[1,2,3],[3,8,4],[5,3,5]]
ans = Solution().minimumEffortPath( heights)
print(ans)