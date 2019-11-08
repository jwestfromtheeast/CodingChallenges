from heapq import heapify, heappush, heappop, heapreplace, heappushpop
class Solution:
    # Complexity Time: O(nlogk), Space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for i in range(k, len(nums)):
            heappushpop(heap, nums[i])
        return heap[0]

    # Complexity: Time O(nlogn), Space: O(n)
    def findKthLargestSort(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]