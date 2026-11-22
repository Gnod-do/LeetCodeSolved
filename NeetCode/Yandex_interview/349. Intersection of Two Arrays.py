class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        setN = set()
        for i in range(len(nums1)):
            if nums1[i] not in setN:
                setN.add(nums1[i])

        res = []
        for i in range(len(nums2)):
            if nums2[i] in setN:
                res.append(nums2[i])
                setN.remove(nums2[i])

        return res

    '''
    hoac chi don gian la: return list(set(nums1) & set(nums2))
    '''