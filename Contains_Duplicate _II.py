class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i,n in enumerate(nums):
            if n in dic:
                return True
            dic[n] = i
            if i >= k:
                old = nums[i-k]
                del dic[old]
        return False

solution = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(solution.containsNearbyDuplicate(nums, k))


#Note: Mấy bài duplicate này nên dùng hashmap để giảm độ phức tạp xuống O(n)
