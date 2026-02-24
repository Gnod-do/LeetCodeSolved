class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        col = set()
        diagPo = set()
        diagNe = set()
        cur = [['.'] * n for _ in range(n)]

        def backtrack(r, diagPo, diagNe):
            if r == n:
                copy = ["".join(row) for row in cur]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r - c) in diagPo or (r + c) in diagNe:
                    continue

                col.add(c)
                diagPo.add(r - c)
                diagNe.add(r + c)
                cur[r][c] = "Q"
                backtrack(r + 1, diagPo, diagNe)

                # backtrack
                col.remove(c)
                diagPo.remove(r-c)
                diagNe.remove(r+c)
                cur[r][c] = "."

        backtrack(0, diagPo, diagNe)
        return res

n = 4
sol = Solution()
print(sol.solveNQueens(n))