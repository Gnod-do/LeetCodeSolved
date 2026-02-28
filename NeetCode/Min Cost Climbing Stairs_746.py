class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        # def recur(i):
        #     if i < 2:
        #         return 0
        #     return min(cost[i-1] + recur(i-1),
        #                cost[i-2] + recur(i-2))
        # return recur(n)
        dp = [0] * (n+1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n]


cost = [10,15,20]
sol = Solution()
print(sol.minCostClimbingStairs(cost))