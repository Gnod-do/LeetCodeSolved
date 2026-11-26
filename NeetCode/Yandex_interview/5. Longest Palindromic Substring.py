class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1

        start, end = 0, 0

        for i in range(len(s)):
            for l,r in (expand(i,i), expand(i, i+1)):
                if r - l > end - start:
                    start, end = l, r

        return s[start:end+1]


s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))