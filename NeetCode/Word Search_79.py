class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board), len(board[0])

        def dfs(board, word, pos, wIndex):
            i,j = pos
            if wIndex == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[wIndex]:
                return False

            tmp = board[i][j]
            board[i][j] = "#"
            res = (dfs(board, word,(i+1, j),wIndex + 1) or
                   dfs(board, word,(i-1, j),wIndex + 1) or
                   dfs(board, word,(i, j + 1),wIndex + 1) or
                   dfs(board, word,(i, j - 1),wIndex + 1))

            board[i][j] = tmp
            return res



        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(board, word, (i,j),0): return True

        return False




board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
sol = Solution()
print(sol.exist(board, word))