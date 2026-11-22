from collections import defaultdict


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        cnt = defaultdict(int)

        for x in nums1:
            cnt[x] += 1

        res = []
        for x in nums2:
            if cnt[x] > 0:
                res.append(x)
                cnt[x] -= 1
        return res


    '''
    hoac sort 2 arrays roi dung 2 con tro dat o moi dau cua day.
    '''