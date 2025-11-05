class Solution(object):
    def maxArea(self, height):
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] > height[right]:
                tmp = height[right] * (right - left)
                right -= 1
            else:
                tmp = height[left] * (right - left)
                left += 1
            res = max(res, tmp)
        return res

solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))
