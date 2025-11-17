class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

nums = [0,3,7,2,5,8,4,6,0,1]
sol = Solution()
print(sol.longestConsecutive(nums))