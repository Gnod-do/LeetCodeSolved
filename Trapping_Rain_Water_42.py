class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        res = 0
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]

        return res



sol = Solution()
height = [5,5,1,7,1,1,5,2,7,6]
print(sol.trap(height))