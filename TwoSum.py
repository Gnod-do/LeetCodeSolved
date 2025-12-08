class Solution:
    def twosum(self, nums, target):
        dic = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff],i]
            dic[n] = i


twosum = Solution()
nums = [2, 7, 11, 15]
target = 20
print(twosum.twosum(nums, target))