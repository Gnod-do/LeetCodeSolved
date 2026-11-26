from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""

        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1

        best_len, start = float("inf"), 0
        missing = len(t)
        left = 0
        for i, x in enumerate(s):
            if cnt[x] > 0:
                missing -= 1

            cnt[x] -= 1

            while missing == 0:
                if i - left + 1 < best_len:
                    best_len = i - left + 1
                    start = left

                y = s[left]
                cnt[y] += 1
                if cnt[y] > 0:
                    missing += 1
                left += 1

        if best_len == float("inf"):
            return ""

        return s[start: start + best_len]






s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))