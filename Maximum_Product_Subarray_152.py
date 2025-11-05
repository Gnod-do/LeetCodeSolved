class Solution(object):
    def maxProduct(self, nums):
        maxProd = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], currMax * nums[i], currMin * nums[i])
            currMin = min(nums[i], currMax * nums[i], currMin * nums[i])
            currMax = temp

            maxProd = max(maxProd, currMax)
        return maxProd

    def maxProductTraversingBothDirections(self, nums):
        leftProd, rightProd = 1, 1
        maxProd = float('-inf')

        for i in range(len(nums)):
            if leftProd == 0:
                leftProd = 1
            elif rightProd == 0:
                rightProd = 1

            leftProd *= nums[i]

            j = len(nums) - i - 1
            rightProd *= nums[j]
            maxProd = max(maxProd, leftProd, rightProd)
        return maxProd


#Hướng tiếp cận này được gọi là: Greedy Min-Max Product với độ phức tạp O(n) và space O(1)

sol = Solution()
nums = [-2, 6, -3, -10, 0, 2]
print(sol.maxProduct(nums))
print(sol.maxProductTraversingBothDirections(nums))