class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []



numbers = [-1,0]
target = -1
sol = Solution()
print(sol.twoSum(numbers, target))