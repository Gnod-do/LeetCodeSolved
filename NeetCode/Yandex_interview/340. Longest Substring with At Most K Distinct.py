from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = defaultdict(int)

        left = res = 0

        for right, x in enumerate(s):
            cnt[x] += 1

            while len(cnt) > k:
                y = s[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                left += 1

            res = max(res, right - left + 1)

        return res


s = "eceba"
k = 2
sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct(s, k))