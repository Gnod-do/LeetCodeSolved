import collections
from collections.abc import Collection


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        dp = collections.deque()

        for i in range(len(nums)):
            # 1. Remove element's out of bound
            if dp and dp[0] == i - k:
                dp.popleft()

            # 2. Remove element's smaller
            while dp and nums[dp[-1]] < nums[i]:
                dp.pop()

            # 3. Add index
            dp.append(i)

            # 4. Add max left to res
            if i + 1 >= k:
                res.append(nums[dp[0]])
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums, k))