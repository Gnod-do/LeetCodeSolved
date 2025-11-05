class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        n = len(nums)
        return max(nums[0] * nums[1] * nums[n-1], nums[n-1] * nums[n-2] * nums[n-3])


'''
Constraints:
+) 3 <= nums.length <= 104
+) -1000 <= nums[i] <= 1000
'''
sol = Solution()
nums = [-100,-98,-1,2,3,4] #39200
print(sol.maximumProduct(nums))
