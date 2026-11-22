from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = defaultdict(int)
        cnt[0] = 1
        s = 0
        res = 0

        for num in nums:
            s += num
            res += cnt[s - k]
            cnt[s] += 1

        return res

nums = [1, 1, 1]
k = 2

sol = Solution()
print(sol.subarraySum(nums, k))