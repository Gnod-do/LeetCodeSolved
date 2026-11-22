class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)

        if n != m:
            return False

        dic = {}
        dic2 = {}
        for i in range(n):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False

            dic[s[i]] = t[i]
            dic2[t[i]] = s[i]

        if len(dic) != len(dic2):
            return False
        return True

