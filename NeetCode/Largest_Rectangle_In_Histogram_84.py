class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea

heights = [7,1,7,2,2,4]
sol = Solution()
print(sol.largestRectangleArea(heights))