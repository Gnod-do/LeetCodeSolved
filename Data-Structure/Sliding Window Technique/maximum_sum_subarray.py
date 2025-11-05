class Solution:
    def maxSum(self, nums, k):
        n = len(nums)
        maxSum = 0

        for i in range(n - k + 1):
            currSum = 0
            for j in range(k):
                currSum += nums[i + j]

            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSumUsingSlidingWindow(self, nums, k):
        n = len(nums)

        windowSum = sum(nums[:k])
        maxSum = windowSum

        for i in range(n - k):
            windowSum = windowSum - nums[i] + nums[i+ k]
            maxSum = max(maxSum, windowSum)

        return maxSum


'''
Time Complexity: O(n * k)
Space Complexity: O(1)

Time Complexity: O(n)
Space Complexity: O(1)
'''
sol = Solution()
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(sol.maxSum(nums, k))
print(sol.maxSumUsingSlidingWindow(nums, k))