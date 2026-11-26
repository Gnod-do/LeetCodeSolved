class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            s, t = t, s

        n, k = len(s), len(t)

        if k - n > 1:
            return False

        for i in range(n):
            if s[i] != t[i]:
                if n == k:
                    return s[i+1:] == t[i+1:]
                return s[i:] == t[i+1:]

        return k - n == 1




s = "a"
t = "A"
sol = Solution()
print(sol.isOneEditDistance(s, t))