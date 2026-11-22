from collections import defaultdict

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        cnt = defaultdict(int)
        common = 0
        C = [0] * len(A)

        for i in range(len(A)):
            cnt[A[i]] += 1
            cnt[B[i]] += 1
            if cnt[A[i]] == 2:
                common += 1
            if cnt[B[i]] == 2:
                common += 1
            if A[i] == B[i]:
                common -= 1

            C[i] = common

        return C
