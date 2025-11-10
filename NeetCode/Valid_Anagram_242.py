'''
Given two strings s and t, return true if the two strings are anagrams
of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"
Output: true
'''


class Solution:
    def isAnagram(self, s,t):
        dic1 = {}
        dic2 = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1


        for ch in t:
            if ch in dic2:
                dic2[ch] += 1
            else:
                dic2[ch] = 1

        for ch in dic1:
            if ch not in dic2:
                return False
            elif dic1[ch] != dic2[ch]:
                return False

        return True


s = "jar"
t = "jam"
sol = Solution()
print(sol.isAnagram(s,t))
