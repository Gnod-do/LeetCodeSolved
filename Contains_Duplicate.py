class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i,n in enumerate(nums):
            if n in dic:
                return True
            dic[n] = i
        return False

solution = Solution()
nums = [1,2,3,1]
print(solution.containsDuplicate(nums))
