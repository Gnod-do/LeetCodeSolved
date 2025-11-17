class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
        unique_tuples = set(tuple(nums) for nums in res)
        res_unique = [list(t) for t in unique_tuples]
        return res_unique


nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))


