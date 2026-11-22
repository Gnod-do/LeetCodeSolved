class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        res = [1] * n
        for i in range(n):
            res[i] = postfix[i] * prefix[i]

        return res

nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))