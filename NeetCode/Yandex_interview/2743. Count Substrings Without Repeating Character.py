from collections import defaultdict

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        left = res = 0

        for right in range(len(s)):
            cnt[s[right]] += 1

            while cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1

            res += right - left + 1
        return res


s = "abcdefghijklmnopqrstuvwxyz"
sol = Solution()
print(sol.numberOfSpecialSubstrings(s))