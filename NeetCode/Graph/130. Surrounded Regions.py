from collections import deque


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    queue.append((r, c))
                    board[r][c] = 'T'

        while queue:
            r, c = queue.popleft()

            for i, j in directions:
                new_r, new_c = r + i, c + j

                if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == 'O':
                    board[new_r][new_c] = 'T'
                    queue.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

