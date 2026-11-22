class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        poins = [0] * (max(nums) + 1)

        for x in nums:
            poins[x] += x

        dp = [0] * (max(nums) + 1)

        dp[0] = poins[0]
        dp[1] = max(poins[0], poins[1])

        for i in range(2, len(poins)):
            dp[i] = max(poins[i] + dp[i - 2], dp[i - 1])

        return dp[-1]