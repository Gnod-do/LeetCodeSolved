class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1 = [nums[0], max(nums[0], nums[1])]
        dp2 = [nums[1], max(nums[1], nums[2])]

        for i in range(3, n):
            curr = max(dp2[-1], nums[i] + dp2[-2])
            dp2.append(curr)

        for i in range(2,n - 1):
            curr = max(dp1[-1], nums[i] + dp1[-2])
            dp1.append(curr)

        return max(dp1[-1], dp2[-1])

nums = [1,2,3,1]
solution = Solution()
print(solution.rob(nums))