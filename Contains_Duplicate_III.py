class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}
        for i,n in enumerate(nums):
            bucket_id = n // bucket_size

            if bucket_id in buckets:
                return True

            if (bucket_id - 1) in buckets and abs(buckets[bucket_id - 1] - n) <= valueDiff:
                return True

            if (bucket_id + 1) in buckets and abs(buckets[bucket_id + 1] - n) <= valueDiff:
                return True

            buckets[bucket_id] = n

            if i >= indexDiff:
                old_bucket = nums[i - indexDiff]
                old_bucket_id = old_bucket // bucket_size
                if old_bucket_id in buckets:
                    del buckets[old_bucket_id]

        return False
nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3

solution = Solution()
print(solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))