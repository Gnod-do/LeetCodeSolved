class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        count = 0

        for i in range(n):
            for j in range(2):
                left, right = i, i + j

                while left >=0 and right < n and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count



s = "aaa"
solution = Solution()
print(solution.countSubstrings(s))