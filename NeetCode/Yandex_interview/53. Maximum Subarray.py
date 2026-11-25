class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = best = nums[0]

        for num in nums[1:]:
            cur = max(num, cur + num)
            best = max(best, cur)

        return best

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(nums))