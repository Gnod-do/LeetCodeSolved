class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def dfs(index, cur):
            if index == len(nums):
                res.append(cur[:])
                return

            cur.append(nums[index])
            dfs(index + 1, cur)
            cur.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1, cur)

        dfs(0, [])
        return res



nums = [1,2,2]
solution = Solution()
res = solution.subsetsWithDup(nums)
print(res)