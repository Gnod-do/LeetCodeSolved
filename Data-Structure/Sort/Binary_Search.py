class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def binaryRecursive(self, nums, left, right, target):
        if left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return self.binaryRecursive(nums, left, mid - 1, target)
            else:
                return self.binaryRecursive(nums, mid + 1, right, target)
        else:
            return -1



nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 38
sol = Solution()
print(sol.binarySearch(nums, target))
print(sol.binaryRecursive(nums, 0, len(nums) - 1, target))