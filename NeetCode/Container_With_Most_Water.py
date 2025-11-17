class Solution:
    def maxArea(self, heights):
        maxArea = 0
        left, right = 0, len(heights)-1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(area, maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea

height=[1,7,2,5,4,7,3,6]
sol = Solution()
print(sol.maxArea(height))
