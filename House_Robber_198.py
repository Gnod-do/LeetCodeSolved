class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0

        # [rob1,rob2,n,n+1,...]
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1, rob2 = rob2, tmp
        return rob2

nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))