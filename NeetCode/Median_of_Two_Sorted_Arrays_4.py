class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A,B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A

        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

nums1 = [1,3]
nums2 = [2]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))