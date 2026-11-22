class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        l = r = 0

        if not nums:
            return []
        res = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - 1 != nums[i]:
                if l != r:
                    res.append(f"{nums[l]}->{nums[r]}")
                else:
                    res.append(f"{nums[l]}")
                r += 1
                l = r
            else:
                r += 1

        if l != r:
            res.append(f"{nums[l]}->{nums[r]}")
        else:
            res.append(f"{nums[l]}")
        return res