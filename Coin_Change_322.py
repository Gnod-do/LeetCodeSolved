class Solution(object):
    def coinChange(self, coins, amount):
        large_int = 10 ** 9
        dp = [large_int] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != large_int else -1


sol = Solution()
coins = [2]
amount = 3
print(sol.coinChange(coins,amount))