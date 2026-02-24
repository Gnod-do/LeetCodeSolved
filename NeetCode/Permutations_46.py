class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        solution = []
        def dfs():
            if len(solution) == len(nums):
                res.append(solution[:])
                return

            for num in nums:
                if not num in solution:
                    solution.append(num)
                    dfs()
                    solution.pop()
        dfs()
        return res

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))