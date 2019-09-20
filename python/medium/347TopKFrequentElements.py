# Leetcode 347
class Solution:
    # Bucket sort
    # Complexity: Time O(n) Space O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freq = {}
        for a in nums:
            curr = freq.get(a, 0) + 1
            freq[a] = curr
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in freq.items():
            bucket[value].append(key)
        ans = []
        for lst in reversed(bucket):
            ans.extend(lst)
            if len(ans) >= k:
                return ans[:k]
        return ans[:k]