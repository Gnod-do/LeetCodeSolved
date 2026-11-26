from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = defaultdict(int)
        left = best = 0

        for right, char in enumerate(s):
            dict[char] += 1

            while dict[char] > 1:
                dict[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best
