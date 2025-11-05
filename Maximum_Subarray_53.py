class Solution(object):
    def maxSubArray(self, nums):

        maxEnding = nums[0]

        res = nums[0]

        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        return res

#Ở đây dùng Kadane's Algorithm với độ phức tạp O(n) và space complexity O(1)

sol = Solution()
nums = [5,4,-1,7,8]
print(sol.maxSubArray(nums))