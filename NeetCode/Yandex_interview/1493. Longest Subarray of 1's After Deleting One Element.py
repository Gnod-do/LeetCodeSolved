class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = best = zeros = 0

        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1

                left += 1
            best = max(best, right - left)

        return best