class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
        unique_tuples = set(tuple(sublist) for sublist in res)
        unique_lists = [list(t) for t in unique_tuples]
        return unique_lists

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))