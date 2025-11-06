class Solution(object):
    def combinationSum4(self, nums, target):
        dp = {0 : 1}

        for i in range(1, target + 1):
            dp[i] = 0
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]

        return dp[target]


#bài này thì vẽ decision tree ra. Thấy các giải pháp lặp lại thì mình sẽ suy nghĩ đến việc dùng
#dynamic programming. Chỗ dp[0] = 1 vì chọn none từ [] để sum = 0. Tóm lại thì dp[n] = tổng tất cả
# các nhánh, cách của cây con.
sol = Solution()
nums = [9]
target = 3
print(sol.combinationSum4(nums, target))