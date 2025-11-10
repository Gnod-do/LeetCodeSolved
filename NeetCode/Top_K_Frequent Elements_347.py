class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n,0)

        for key,v in counts.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




nums = [1,2,2,3,3,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))