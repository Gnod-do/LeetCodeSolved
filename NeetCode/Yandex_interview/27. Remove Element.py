class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w = 0

        for x in nums:
            if x != val:
                nums[w] = x
                w += 1

        return w