class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        k = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[k] = nums[left] ** 2
                left += 1
            else:
                res[k] = nums[right] ** 2
                right -= 1
            k -= 1

        return res

nums = [-7, -3, 2, 3, 11]
res = Solution().sortedSquares(nums)
print(res)