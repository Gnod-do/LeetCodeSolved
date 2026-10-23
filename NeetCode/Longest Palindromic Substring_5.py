class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        start, maxLen = 0, 1

        for i in range(n):
            for j in range(2):
                left, right = i, i + j
                while left >= 0 and right < n and s[left] == s[right]:
                    currLen = right - left + 1
                    if currLen > maxLen:
                        maxLen = currLen
                        start = left
                    left -= 1
                    right += 1
        return s[start:start + maxLen]


s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))