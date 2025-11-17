class Solution(object):
    def trap(self, height):
        res = 0
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[0], height[-1]

        while left < right:
            if maxLeft > maxRight:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
            else:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]

        return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))