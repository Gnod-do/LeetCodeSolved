class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = dec = res = 1

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                inc += 1
                dec = 1
            elif nums[i+1] < nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            res = max(res, inc, dec)
        return res