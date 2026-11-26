class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        win = [0] * 26
        need = [0] * 26
        n, k = len(s), len(p)
        res = []
        for c in p:
            need[ord(c) - ord('a')] += 1

        for i in range(n):
            win[ord(s[i]) - ord('a')] += 1

            if i >= k:
                win[ord(s[i - k]) - ord('a')] -= 1

            if i >= k - 1 and win == need:
                res.append(i - k + 1)

        return res


s = "cbaebabacd"
p = "abc"

sol = Solution()
print(sol.findAnagrams(s, p))