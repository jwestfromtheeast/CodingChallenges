class Solution:
    # Original solution
    # Complexity: O(n) time, O(n) space
    def maxSubArrayy(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sums = [nums[i] for i in range(len(nums))]
        max_sum = sums[0]
        for i in range(1, len(nums)):
            sums[i] = max(nums[i], nums[i] + sums[i - 1])
            max_sum = max(max_sum, sums[i])
        return max_sum
    
    # Notice we only ever access current and previous elements, so can reduce space
    # Complexity: O(n) time, O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], nums[i] + curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum