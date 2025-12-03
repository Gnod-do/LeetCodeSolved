class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) -ord("a")] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[i]) - ord("a")] += 1
            s2_counts[ord(s2[i - len(s1)]) -ord("a")] -= 1

            if s1_counts == s2_counts:
                return True
        
        return False
s1 = "ab"
s2 = "eidbeaooo"

sol = Solution()
print(sol.checkInclusion(s1, s2))