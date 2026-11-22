class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev = -1
        pre = mid = pos = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    pre = i
                else:
                    mid = max(mid, (i - prev) // 2)

                prev = i
        pos = len(seats) - 1 - prev
        return max(pre, mid, pos)