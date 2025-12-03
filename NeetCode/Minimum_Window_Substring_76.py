class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1,-1], float("inf")

        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                #Update the result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                #Pop Left pointer
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""






s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))