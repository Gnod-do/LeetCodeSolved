class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


        return -1

sol = Solution()
nums = [4,5,6,1,2,3]
print(sol.findMin(nums))