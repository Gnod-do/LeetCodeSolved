class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or index == len(candidates):
                return

            # include candidates[i]
            cur.append(candidates[index])
            dfs(index + 1, cur , total + candidates[index])
            cur.pop()

            # not include candidates[i]
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, cur, total)

        dfs(0,[],0)
        return res


candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))