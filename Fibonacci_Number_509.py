class Solution(object):
    def fib(self, n):
        curr = 0
        prev1 = 0
        prev2 = 1
        if n <= 1:
            return n
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        return curr

sol = Solution()
n = 2
print(sol.fib(n))